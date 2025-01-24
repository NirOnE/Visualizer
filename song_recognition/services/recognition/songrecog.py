import asyncio
import os
from song_recognition.config.settings import sPaths
from song_recognition.services.record.audio_record import AudioRecorder
from song_recognition.services.recognition.acrcloud import ACRCloudRecognitionService
from song_recognition.services.recognition.shazam import ShazamRecognitionService
from song_recognition.services.artwork.lastfm import LastFMArtworkService
from icecream import ic

class SongRecognitionApp:
    def __init__(self):
        self.recorder = AudioRecorder()
        self.recognition_services = [
#            ACRCloudRecognitionService(),
            ShazamRecognitionService()
        ]
        self.artwork_service = LastFMArtworkService()
    
    async def recognize_song(self):
        # Record audio
        audio_path = self.recorder.record()
        
        # Try recognition services
        for service in self.recognition_services:
            song = await service.recognize(audio_path)
            
            if song and song.is_recognized():
                # Fetch artwork if not already available
                if not song.artwork_url:
                    song.artwork_url = self.artwork_service.get_artwork_url(
                        song.album, song.artist
                    )
                song.save_artwork(sPaths.DATA_DIR)
                return song
        
        return None

if __name__ == '__main__':

    recording = SongRecognitionApp()
    recording.record_music()
    recording.analyse_music()
    ic(recording.song_name, recording.album_name,
       recording.artist, recording.artwork_url)
