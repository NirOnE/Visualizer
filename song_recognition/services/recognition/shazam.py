from shazamio import Shazam
from song_recognition.core.model import Song
from song_recognition.core.exceptions import RecognitionServiceError
from song_recognition.services.recognition.base import BaseRecognitionService
from typing import Optional

class ShazamRecognitionService(BaseRecognitionService):
    async def recognize(self, audio_path: str) -> Optional[Song]:
        try:
            shazam = Shazam()
            out = await shazam.recognize_song(audio_path)
            
            if out.get('matches'):
                track = out.get('track', {})
                sections = track.get('sections', [])
                
                artist = sections[0]['metapages'][0].get('caption', 'Unknown')
                title = sections[0]['metapages'][1].get('caption', 'Unknown')
                
                return Song(
                    artist=artist,
                    title=title,
                    album=sections[0]['metadata'][0].get('text', 'Unknown'),
                    artwork_url=track.get('images', {}).get('coverarthq')
                )
            
            return None
        
        except Exception as e:
            raise RecognitionServiceError(f"Shazam recognition failed: {e}")