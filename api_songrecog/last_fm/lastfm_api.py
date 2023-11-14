import requests
import pylast
import os
from icecream import ic
from dotenv import load_dotenv
load_dotenv()

_api_key = os.getenv("API_KEY")
_api_secret = os.getenv("API_SECRET")
_username = os.getenv("USERNAME")

password_hash = pylast.md5("PASS")

network = pylast.LastFMNetwork(
    api_key=_api_key,
    api_secret=_api_secret,
    username=_username)

# SESSION_KEY_FILE = os.path.join(os.path.expanduser("~"), ".session_key")
# network = pylast.LastFMNetwork(API_KEY, API_SECRET)
# if not os.path.exists(SESSION_KEY_FILE):
#     skg = pylast.SessionKeyGenerator(network)
#     url = skg.get_web_auth_url()

#     print(f"Please authorize this script to access your account: {url}\n")
#     import time
#     import webbrowser

#     webbrowser.open(url)

#     while True:
#         try:
#             session_key = skg.get_web_auth_session_key(url)
#             with open(SESSION_KEY_FILE, "w") as f:
#                 f.write(session_key)
#             break
#         except pylast.WSError:
#             time.sleep(1)
# else:
#     session_key = open(SESSION_KEY_FILE).read()

# network.session_key = session_key


def get_album_artwork(album_name, artist) -> str:

    album = network.get_album(title=album_name, artist=artist)
    ic(album)
    img = album.get_cover_image(size=3)
    ic(img)
    return img


if __name__ == "__main__":
    album_name = 'Kind of blue'
    artist = 'Miles Davis'
    ic(get_album_artwork(album_name=album_name, artist=artist))
