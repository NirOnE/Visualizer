from dataclasses import dataclass
from typing import Optional
import urllib.request
from .exceptions import ArtworkError
from pathlib import Path
from icecream import ic

@dataclass
class Song:
    """Represents a recognized song with its metadata"""
    title: str = ''
    artist: str = ''
    album: str = ''
    artwork_url: Optional[str] = None

    def save_artwork(self, directory: Path) -> Path:
        """Downloads and saves artwork to specified directory"""
        if not self.artwork_url:
            raise ArtworkError("No artwork URL available")

        filename = f"{self.album}_{self.artist}.jpg".replace(" ", "")
        path = directory +"/"+ filename
        try:
            urllib.request.urlretrieve(self.artwork_url, path)
            self.artwork_path = path
            return path
        except Exception as e:
            raise ArtworkError(f"Failed to download artwork: {e}")

    def __str__(self) -> str:
        return f"{self.title} by {self.artist} (from {self.album})"

    def is_recognized(self) -> bool:
        """Check if the song has been successfully recognized"""
        return (self.artist != "Unknown" and self.title != "Unknown")
