from abc import ABC, abstractmethod
from typing import Optional

class BaseArtworkService(ABC):
    """Abstract base class for album artwork retrieval services"""
    
    @abstractmethod
    def get_artwork_url(self, album_name: str, artist: str) -> Optional[str]:
        """
        Retrieve album artwork URL
        
        Args:
            album_name (str): Name of the album
            artist (str): Name of the artist
        
        Returns:
            Optional[str]: URL of the artwork or None if not found
        """
        pass
