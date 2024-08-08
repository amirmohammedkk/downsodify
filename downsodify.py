import requests
import base64
from time import time
import yt_dlp as youtube_dl
import os
import tkinter as tk
from tkinter import filedialog


client_id = '1235a099db14421da0ce42238938c36a'
client_secret = '49e9ab63d17c42d19108c5379fe8506f'

token_url = 'https://accounts.spotify.com/api/token'
access_token = None
token_expiry = 0  

save_directory = None

def get_access_token():
    global access_token, token_expiry

    if access_token and time() < token_expiry:
        return access_token  

    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode(),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }

    try:
        response = requests.post(token_url, headers=headers, data=data)

        if response.status_code == 200:
            token_info = response.json()
            access_token = token_info['access_token']
            token_expiry = time() + token_info['expires_in']  
            return access_token
        else:
            print(f"Failed to retrieve access token: {response.status_code}")
            print(response.text)
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error during token retrieval: {e}")
        return None

def parse_spotify_url(url):
    if 'album' in url:
        return 'album'
    elif 'playlist' in url:
        return 'playlist'
    elif 'track' in url:
        return 'track'
    else:
        print("Invalid Spotify URL. Could not determine resource type.")
        return None

def get_resource_tracks(resource_type, resource_id):
    global access_token

    if resource_type not in ['album', 'playlist', 'track']:
        print(f"Invalid resource type '{resource_type}'. Supported types: 'album', 'playlist', 'track'.")
        return None

    url = f'https://api.spotify.com/v1/{resource_type}s/{resource_id}/tracks'
    headers = {
        'Authorization': f'Bearer {get_access_token()}'
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()['items']
        elif response.status_code == 401:
            access_token = None  
            headers['Authorization'] = f'Bearer {get_access_token()}'
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                return response.json()['items']
            else:
                print(f"Failed to fetch {resource_type} tracks after token refresh: {response.status_code}")
                print(response.text)
                return None
        else:
            print(f"Failed to fetch {resource_type} tracks: {response.status_code}")
            print(response.text)
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error during {resource_type} tracks retrieval: {e}")
        return None

def print_track_info(track):
    track_name = track['name']
    artists = ', '.join([artist['name'] for artist in track['artists']])
    duration_ms = track['duration_ms']

    duration_min = duration_ms / 1000 / 60
    duration_sec = (duration_min - int(duration_min)) * 60
    duration_str = f"{int(duration_min)}:{int(duration_sec):02d}"  

    print(f"Track Name: {track_name}")
    print(f"Artists: {artists}")
    print(f"Duration: {duration_str}")

    search(track_name, artists)

def search(track_name, artists):
    query = f"{track_name} {artists}"
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(save_directory, '%(title)s.%(ext)s'),  
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        search_result = ydl.extract_info(f"ytsearch:{query}", download=False)
        
        if 'entries' in search_result:
            video = search_result['entries'][0]
            video_url = video['webpage_url']
            print(f"URL: {video_url}")

            download_audio(video_url)
        else:
            print("No results found")    

def download_audio(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(save_directory, '%(title)s.%(ext)s'),  
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def select_save_directory():
    global save_directory
    root = tk.Tk()
    root.withdraw()  
    save_directory = filedialog.askdirectory(title="Select Save Directory")
    if not save_directory:
        print("No directory selected. Exiting.")
        exit()

if __name__ == '__main__':
    select_save_directory()  
    
    spotify_url = input("Enter Spotify URL: ")

    resource_type = parse_spotify_url(spotify_url)
    
    if resource_type:
        resource_id = spotify_url.split('/')[-1].split('?')[0]

        resource_tracks = get_resource_tracks(resource_type, resource_id)

        if resource_tracks:
            for track in resource_tracks:
                print_track_info(track['track'] if resource_type == 'playlist' else track)
        else:
            print(f"Failed to fetch {resource_type} tracks.")
