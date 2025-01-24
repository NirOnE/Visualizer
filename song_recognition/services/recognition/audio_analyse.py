from dotenv import load_dotenv
import os
from icecream import ic
import acrcloud
from shazamio import Shazam
import asyncio
from song_recognition.core.exceptions import ApiError
from song_recognition.services.recognition.functions_arcloud import get_all_keys_with_positions, get_keys, get_value_for_key, escape_ansi

load_dotenv()


_spot_client_id = os.getenv("SPOTIFY_CLIENT_ID")
_spot_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
_acrcloud_client_id = os.getenv("ACRCLOUD_CLIENT_ID")
_acrcloud__client_secret = os.getenv("ACRCLOUD_CLIENT_SECRET")
_acrcloud__client_host = os.getenv("ACRCLOUD_CLIENT_HOST")

# ic(_spot_client_id)
# ic(_spot_client_secret)
# ic(_acrcloud_client_id)
# ic(_acrcloud__client_secret)
# ic(_acrcloud__client_host)


def analyze_audio_acr(mdatas: {}) -> int: # type: ignore
    """ Analyse the song track and get the metadata from AcrCloud

    Args:
        mdatas (_type_): dict of songs metadata

    Raises:
        ApiError: _description_

    Returns:
        int: error if any or 0 if sucess
    """

    config = {
        "key": _acrcloud_client_id,
        "secret": _acrcloud__client_secret,
        "host": _acrcloud__client_host
    }

    audio = "data/tmp_recording.wav"
    ic(audio)
    acr = acrcloud.ACRcloud(config)
    audio = acr.recognize_audio(audio)

    ic("------", audio)

    target_key = 'code'
    error_code = get_value_for_key(audio, target_key)

    if error_code is not None:
        print(f"The value for the key '{target_key}' is: {error_code}")
    else:
        print(
            f"The key '{target_key}' was not found in the nested dictionary.")

    try:
        if error_code == 0:
            # Recognition succeeded
            result = "Recognition succeed"
            ic(result)
            # result = get_keys(audio)
            # for key in result:
            #     ic(f'{key}')

            title = audio['metadata']['music'][0]['title']
            artist = audio['metadata']['music'][0]['artists'][0].get('name')
            album = audio['metadata']['music'][0]['album'].get('name')

            mdatas['artist'] = escape_ansi(artist)
            mdatas['song_name'] = escape_ansi(title)
            mdatas['album_name'] = escape_ansi(album)
            # artist = audio['metadata']['music'][0]['external_metadata']['spotify']['artists'].get('name')
            # album = audio['metadata']['music'][0]['external_metadata']['spotify']['album'].get('name')

            ic(title)
            ic(artist)
            ic(album)
            return error_code

        elif error_code == 1001:
            # No recognition
            result = "No recognition"
            ic(result)
            return error_code
        elif error_code == 2000:
            # Recording error (device may not have permission)
            result = "Recording error (device may not have permission)"
            ic(result)
            return error_code
        elif error_code == 2001:
            # Init failed or request timeout
            result = "Init failed or request timeout"
            ic(result)
            return error_code
        else:
            raise ApiError(error_code)

    except ApiError as api_error:
        result = str(api_error)
        ic(result)
        return error_code


async def analyze_audio_shaz(mdatas: {}) -> int: # type: ignore
    """analyse the song track and get the metadata from Spotify

    Args:
        mdatas (_type_): dict of songs metadata

    Returns:
        error
    """

    shazam = Shazam()
    out = await shazam.recognize_song("data/tmp_recording.wav")
    ic('-------------- SHAZAM---------------------------')
    #   ic(out)
    #   ic(out['matches'])
    if out['matches']:
        try:
            title = out['track']['sections'][0]['metapages'][1].get('caption')
        except:
            title = ''
        artist = out['track']['sections'][0]['metapages'][0].get('caption')
        album = out['track']['sections'][0]['metadata'][0]['text']
        artwork = out['track']['images'].get('coverarthq')
        ic('Song: ', out['track']['share']['text'])
        mdatas['artist'] = escape_ansi(artist)
        mdatas['song_name'] = escape_ansi(title)
        mdatas['album_name'] = escape_ansi(album)
        mdatas['artwork'] = artwork
        return 0
    else:
        return 1001

if __name__ == '__main__':
    ic(analyze_audio_acr())
    ic(analyze_audio_shaz())
