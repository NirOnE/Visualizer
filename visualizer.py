import subprocess
import asyncio
from icecream import ic
import urllib.request
import tkinter as tk
from PIL import Image, ImageTk
from song_recognition.config.settings import sPaths
from song_recognition.services.recognition.songrecog import SongRecognitionApp

import os
os.environ['ALSA_LOG'] = 'null'

def main():
    sPaths.ensure_dirs()  # Ensure data directories exist
    
    app = SongRecognitionApp()
    
    loop = asyncio.get_event_loop()
    song = loop.run_until_complete(app.recognize_song())
    
    if song:
        print(f"Recognized Song: {song.title}")
        print(f"Artist: {song.artist}")
        print(f"Album: {song.album}")
        print(f"Artwork: {song.artwork_url}")
        ic(str(song))
    else:
        print("No song recognized.")

# window = tk.Tk()
# img = ImageTk.PhotoImage(Image.open(song_path))
# lbl = tk.Label(window, image = img).pack()
# window.mainloop()

if __name__ == '__main__':
    main()