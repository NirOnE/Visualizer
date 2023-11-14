import asyncio
from api_songrecog.audio_processing import audio_record
from api_songrecog.audio_processing import audio_analyse
from api_songrecog.last_fm import lastfm_api
import io
from icecream import ic


class SongPlayed:

    """ Object song """

    def __init__(self) -> None:
        self._artist = "Unkown"
        self._name = "Unkown"
        self._album = "Unkown"
        self._artwork_link = "Unkown"

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, artist_name: str):
        self._artist = artist_name

    @property
    def song_name(self):
        return self._name

    @song_name.setter
    def song_name(self, song: str):
        self._name = song

    @property
    def album_name(self):
        return self._album

    @album_name.setter
    def album_name(self, album: str):
        self._album = album

    @property
    def artwork_link(self):
        return self._artwork_link

    @artwork_link.setter
    def artwork_link(self, link: str):
        self._artwork_link = link

    def record_music(self) -> None:
        return audio_record.record_audio_mic(input=1)

    def analyse_music(self) -> None:
        mdatas = {'artist': '',
                  'song_name': '',
                  'album_name': ''}
        error = audio_analyse.analyze_audio_acr(mdatas)

        if error == 0:
            self.artist = mdatas['artist']
            self.album_name = mdatas['album_name']
            self.song_name = mdatas['song_name']
            self.artwork_link = lastfm_api.get_album_artwork(
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

        self.artist = mdatas['artist']
        self.album_name = mdatas['album_name']
        self.song_name = mdatas['song_name']
        self.artwork_link = mdatas['artwork']
        return error


if __name__ == '__main__':

    recording = SongPlayed()
    recording.record_music()
    recording.analyse_music()
    ic(recording.song_name, recording.album_name,
       recording.artist, recording.artwork_link)
