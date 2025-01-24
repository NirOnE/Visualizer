import os
import pyaudio
from dotenv import load_dotenv

load_dotenv()

class AudioSettings:
    """Configuration for audio recording parameters"""
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 512
    RECORD_SECONDS = 8
    WAVE_OUTPUT_FILENAME = "temp_recording.wav"

class APIKeys:
    """Centralized API key management"""
    SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
    
    ACRCLOUD_CLIENT_ID = os.getenv("ACRCLOUD_CLIENT_ID")
    ACRCLOUD_CLIENT_SECRET = os.getenv("ACRCLOUD_CLIENT_SECRET")
    ACRCLOUD_CLIENT_HOST = os.getenv("ACRCLOUD_CLIENT_HOST")
    
    LASTFM_API_KEY = os.getenv("API_KEY")
    LASTFM_API_SECRET = os.getenv("API_SECRET")
    LASTFM_USERNAME = os.getenv("USERNAME")

class Paths:
    """Path management for various file operations"""
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(PROJECT_ROOT, "data")
    ARTWORK_DIR = os.path.join(DATA_DIR, "artwork")
    
    @classmethod
    def ensure_dirs(cls):
        """Ensure necessary directories exist"""
        os.makedirs(cls.DATA_DIR, exist_ok=True)
        os.makedirs(cls.ARTWORK_DIR, exist_ok=True)
        

sAudiosettings = AudioSettings()
sPaths = Paths()
sAPIKeys = APIKeys()