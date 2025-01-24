import asyncio
from ..record.audio_record import AudioRecorder
from song_recognition.services.recognition import audio_analyse
from song_recognition.services.artwork import lastfm_api
from song_recognition.core.model import Song

import io
from icecream import ic


class SongPlayed:

    """ Object song """

    def __init__(self) -> None:
        self.song = Song()

    def record_music(self) -> None:
        recorder = AudioRecorder()
        return recorder.record(device_index=1)

    def analyse_music(self) -> None:
        mdatas = {'artist': '',
                  'song_name': '',
                  'album_name': ''}
        error = audio_analyse.analyze_audio_acr(mdatas)

        if error == 0:
            self.song.artist = mdatas['artist']
            self.song.album_name = mdatas['album_name']
            self.song.song_name = mdatas['song_name']
            self.song.artwork_link = lastfm_api.get_album_artwork(
                self.album_name, self.artist)

        return error

    def analyse_music_shazam(self) -> int:
        mdatas = {'artist': '',
                  'song_name': '',
                  'album_name': '',
                  'artwork': ''}
        loop = asyncio.get_event_loop()
        error = loop.run_until_complete(
            audio_analyse.analyze_audio_shaz(mdatas))

        self.song.artist = mdatas['artist']
        self.song.album = mdatas['album_name']
        self.song.title = mdatas['song_name']
        self.song.artwork_url = mdatas['artwork']
        return error


if __name__ == '__main__':

    recording = SongPlayed()
    recording.record_music()
    recording.analyse_music()
    ic(recording.song_name, recording.album_name,
       recording.artist, recording.artwork_link)
