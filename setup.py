import subprocess
import sys
import os

def check_and_install_pip_package(package_name):
    try:
        __import__(package_name)
        print(f"{package_name} is already installed.")
        return True
    except ImportError:
        print(f"{package_name} is not installed. Installing...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            return True
        except subprocess.CalledProcessError:
            print(f"Failed to install {package_name}.")
            return False

def check_ffmpeg():
    """Check if ffmpeg is installed."""
    try:
        subprocess.check_output(["ffmpeg", "-version"])
        print("ffmpeg is already installed.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("ffmpeg is not installed. Attempting to install...")
        if install_ffmpeg():
            print("ffmpeg installed successfully. Verifying installation...")
            return check_ffmpeg()  
        else:
            return False

def install_ffmpeg():
    """Install ffmpeg based on the operating system."""
    try:
        if sys.platform.startswith('linux'):
            if os.geteuid() != 0:
                print("This script requires root privileges to install ffmpeg. Please run with sudo.")
                return False
            subprocess.check_call(["apt-get", "update"])
            subprocess.check_call(["apt-get", "install", "-y", "ffmpeg"])
        elif sys.platform == "darwin":  
            subprocess.check_call(["brew", "install", "ffmpeg"])
        elif sys.platform == "win32":  
            print("Please download and install ffmpeg from https://ffmpeg.org/download.html")
            return False
        else:
            print("Unsupported operating system.")
            return False
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install ffmpeg: {e}")
        return False

def print_welcome_message():
    print("===================================================================================")
    print(".........................................................................................")
    print("...............................................................................................")
    print("                                                                                   ")
    print("     ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗░██████╗░█████╗░██████╗░██╗███████╗██╗░░░██╗")
    print("     ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██╔════╝██╔══██╗██╔══██╗██║██╔════╝╚██╗░██╔╝")
    print("     ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║╚█████╗░██║░░██║██║░░██║██║█████╗░░░╚████╔╝░")
    print("     ██║░░██║██║░░██║░░████╔═████║░██║╚████║░╚═══██╗██║░░██║██║░░██║██║██╔══╝░░░░╚██╔╝░░")
    print("     ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║██████╔╝╚█████╔╝██████╔╝██║██║░░░░░░░░██║░░░")
    print("     ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚═════╝░░╚════╝░╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░")
    print("                                                                                   ")
    print("..............................................................................................")
    print(".........................................................................................")
    print("===================================================================================")

def run_downsodify():
    """Run the downsodify.py script."""
    try:
        subprocess.check_call([sys.executable, 'downsodify.py'])
        print("downsodify.py ran successfully.")
    except subprocess.CalledProcessError:
        print("Failed to run downsodify.py.")

if __name__ == "__main__":
    print_welcome_message()
    
    if not (check_and_install_pip_package("requests") and check_and_install_pip_package("yt_dlp")):
        print("Failed to install one or more Python packages. Exiting.")
        sys.exit(1)

    if not check_ffmpeg():
        print("Failed to install or verify ffmpeg. Exiting.")
        sys.exit(1)
    
    run_downsodify()
