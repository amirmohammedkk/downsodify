</p>

<h1 align="center">Downsodify</h1>
<p align="center">
  A tool to download Spotify tracks by searching for them on YouTube.
  <br/>
  <a href="https://github.com/amirmohammedkk/downsodify/issues">Report Bug</a>
  ·
  <a href="https://github.com/amirmohammedkk/downsodify/issues">Request Feature</a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/amirmohammedkk/downsodify" alt="license"/>
  <img src="https://img.shields.io/github/stars/amirmohammedkk/downsodify" alt="stars"/>
  <img src="https://img.shields.io/github/forks/amirmohammedkk/downsodify" alt="forks"/>
  <img src="https://img.shields.io/github/issues/amirmohammedkk/downsodify" alt="issues"/>
</p>

## Overview

Downsodify is a tool designed to download Spotify tracks by searching for them on YouTube. It is lightweight and supports cross-platform use.

## Features

- **Easy to use:** Just drop the Spotify link—whether it’s a playlist or an album—and download tracks with easy commands. No worries!
- **Cross-platform:** Compatible with Windows, macOS, and Linux.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/amirmohammedkk/downsodify.git
   cd downsodify

## Dependencies

Before running the tool, ensure you have the necessary dependencies installed:

1.  Python 3.7+
2.  ffmpeg (for audio processing)
3.  yt-dlp (for YouTube downloading)
   
You can install the required Python packages using:
  ```bash
  pip install -r requirements.txt
  ```
## Running the program

Start by running downsodify.py to ensure any preliminary setup or configuration is handled:
```bash
python setup.py
```
for the direct running of downsodify,
```
python downsodify.py
```

- **Note:** Private playlists links cant be processed. so make sure to change it to public before entering the link.
## Acknowledgments

- **ffmpeg :** For audio processing.
- **yt-dlp :** For downloading YouTube videos.

## Important Note on API Credentials

This project uses Spotify API credentials that are linked to a specific account. Please be aware of the following:

- **API Rate Limits**: Due to the usage of personal Spotify API credentials, there are limitations on the number of access tokens that can be generated. Excessive token generation may lead to disruptions in service.
- **Credential Management**: If you encounter issues with access tokens, it is likely due to the rate limits imposed on the API. We are working on increasing the token limit to accommodate more users.
- **Current Status**: If you face difficulties with the Spotify integration, please check the [Issues](https://github.com/amirmohammedkk/downsodify/issues) page for updates or potential workarounds.

### How to Use with your credentials

1. **Obtain Your API Credentials**: Ensure you have your own Spotify API credentials. You can obtain them by following the [Spotify API documentation](https://developer.spotify.com/documentation/web-api/).
2. **Configuration**: Replace the placeholder credentials in the code with your own API credentials.

For further assistance or to report issues, please visit the [Issues](https://github.com/amirmohammedkk/downsodify/issues) page.


## Contributing

Contributions are welcome! If you have suggestions or improvements, please submit a [pull request](https://github.com/amirmohammedkk/downsodify/pulls) or open an [issue](https://github.com/amirmohammedkk/downsodify/issues/new/choose).


## Disclaimer
The usage of this software may infringe Spotify's ToS and/or your local legislation. Use it under your own risk.





## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.



   





