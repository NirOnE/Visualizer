# Raspberry Pi Audio Recognition and Album Art Display

This Python project leverages the capabilities of a Raspberry Pi to record audio from its microphone, utilize the Spotify API for song recognition, and then displays the album cover art on a connected 64x64 LED screen.

## Prerequisites

- Raspberry Pi with a connected microphone.
- Spotify Developer Account and API credentials.
- 64x64 LED screen connected to the Raspberry Pi.
- Python 3.11 installed on the Raspberry Pi.

## Setup

1. Clone the repository to your Raspberry Pi:

    ```bash
    git clone https://github.com/NirOnE/Visualizer.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain Spotify API credentials:

    - Create a Spotify Developer Account: [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
    - Create a new application to obtain the `Client ID` and `Client Secret`.

4. Configure the application:

    - Replace `YOUR_SPOTIFY_CLIENT_ID` and `YOUR_SPOTIFY_CLIENT_SECRET` with your actual Spotify API credentials.
    - Store them in an .env file 

## Usage

1. Run the main script:

    ```bash
    python visualizer.py
    ```

2. The script will record audio, use the Spotify API to recognize the song, and display the album cover art on the LED screen.

## Customization

- Adjust the audio recording settings for `audio_record.py` in `settings.py`.
- Modify the LED screen display logic in `led_display.py`.
- Explore additional features and customization based on your preferences.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
