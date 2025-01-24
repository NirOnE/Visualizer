import subprocess
from song_recognition.services.recognition.song_recog import SongPlayed
from icecream import ic
import urllib.request
import tkinter as tk
from PIL import Image, ImageTk


import os


recording = SongPlayed()
recording.record_music()
# recording.analyse_music()
if (recording.analyse_music_shazam() == 0):
    ic(recording.song_name, recording.album_name,
       recording.artist, recording.artwork_link)
    current_path = os.getcwd()
    song_name = (recording.album_name + "_" +
                 recording.artist + ".jpg").replace(" ", "")
    song_path = (current_path + "/data/" + song_name)
    urllib.request.urlretrieve(recording.artwork_link, song_path)
    ic(song_path)
else:
    ic("not recognized")

# window = tk.Tk()
# img = ImageTk.PhotoImage(Image.open(song_path))
# lbl = tk.Label(window, image = img).pack()
# window.mainloop()
