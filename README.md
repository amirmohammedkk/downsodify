# downsodify
A tool to download Spotify tracks by searching for them on YouTube.

## Setup

### Python Dependencies

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/downsodify.git
    cd downsodify
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### System Dependencies

4. Run the setup script to check and install system dependencies:
    ```bash
    python setup.py
    ```

    This will install `ffmpeg` if it is not already installed. Follow any additional prompts to complete the installation.

## Usage

Run the script to start the process:
```bash
python downsodify.py
