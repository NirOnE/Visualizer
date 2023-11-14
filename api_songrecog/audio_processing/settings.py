import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 512
RECORD_SECONDS = 8
WAVE_OUTPUT_FILENAME = "tmp_recording.wav"
PATH_FILE = "./data/"
