import pylast
from typing import Optional
from icecream import ic
from song_recognition.config.settings import sAPIKeys
from song_recognition.services.artwork.base import BaseArtworkService


class LastFMArtworkService(BaseArtworkService):
    def __init__(self):
        self.network = pylast.LastFMNetwork(
            api_key=sAPIKeys.LASTFM_API_KEY,
            api_secret=sAPIKeys.LASTFM_API_SECRET,
            username=sAPIKeys.LASTFM_USERNAME
        )
    
    def get_artwork_url(self, album_name: str, artist: str) -> Optional[str]:
        try:
            album = self.network.get_album(title=album_name, artist=artist)
            return album.get_cover_image(size=3)  # Large cover
        except Exception:
            return None

if __name__ == "__main__":
    album_name = 'Kind of blue'
    artist = 'Miles Davis'
    ic(LastFMArtworkService.get_artwork_url(album_name=album_name, artist=artist))
