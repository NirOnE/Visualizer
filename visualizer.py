import subprocess
from song_recognition.services.recognition.song_recog import SongPlayed
from icecream import ic
import urllib.request
import tkinter as tk
from PIL import Image, ImageTk
from song_recognition.config.settings import sPaths

import os


recording = SongPlayed()
recording.record_music()
# recording.analyse_music()
if (recording.analyse_music_shazam() == 0):
    recording.song.save_artwork(sPaths.DATA_DIR)
    ic(str(recording.song))
    ic(recording.song.artwork_path)
    ic(recording.song.artwork_url)
else:
    ic("not recognized")

# window = tk.Tk()
# img = ImageTk.PhotoImage(Image.open(song_path))
# lbl = tk.Label(window, image = img).pack()
# window.mainloop()
