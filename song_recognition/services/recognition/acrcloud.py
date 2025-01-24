import acrcloud
from song_recognition.config.settings import sAPIKeys
from song_recognition.core.model import Song
from song_recognition.core.exceptions import RecognitionServiceError
from song_recognition.services.recognition.base import BaseRecognitionService
from typing import Optional

class ACRCloudRecognitionService(BaseRecognitionService):
    def __init__(self):
        self.config = {
            "key": sAPIKeys.ACRCLOUD_CLIENT_ID,
            "secret": sAPIKeys.ACRCLOUD_CLIENT_SECRET,
            "host": sAPIKeys.ACRCLOUD_CLIENT_HOST
        }
    
    async def recognize(self, audio_path: str) -> Optional[Song]:
        try:
            acr = acrcloud.ACRcloud(self.config)
            result = acr.recognize_audio(audio_path)
            
            if result.get('status', {}).get('code') == 0:
                music_info = result['metadata']['music'][0]
                
                return Song(
                    artist=music_info['artists'][0].get('name', 'Unknown'),
                    name=music_info.get('title', 'Unknown'),
                    album=music_info.get('album', {}).get('name', 'Unknown')
                )
            
            return None
        
        except Exception as e:
            raise RecognitionServiceError(f"ACRCloud recognition failed: {e}")