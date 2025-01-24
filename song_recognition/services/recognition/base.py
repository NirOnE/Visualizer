from abc import ABC, abstractmethod
from song_recognition.core.model import Song
from typing import Optional

class BaseRecognitionService(ABC):
    """Abstract base class for music recognition services"""
    
    @abstractmethod
    async def recognize(self, audio_path: str) -> Optional[Song]:
        """
        Recognize a song from an audio file.
        
        Args:
            audio_path (str): Path to the audio file to recognize
        
        Returns:
            Optional[Song]: Recognized song or None if recognition fails
        """
        pass