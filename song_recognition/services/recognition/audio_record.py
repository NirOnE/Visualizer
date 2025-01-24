import pyaudio
import wave
from icecream import ic
import os
from song_recognition.config.settings import PATH_FILE, CHANNELS, CHUNK, FORMAT, RATE, RECORD_SECONDS, WAVE_OUTPUT_FILENAME

device_index = 1
audio = pyaudio.PyAudio()

ic(PATH_FILE, CHANNELS, CHUNK, FORMAT, RATE, RECORD_SECONDS, WAVE_OUTPUT_FILENAME)


def list_inputs():
    # To chose input if needed
    ic("----------------------record device list---------------------")
    info = audio.get_host_api_info_by_index(0)
    # numdevices = info.get('deviceCount')
    # for i in range(0, numdevices):
    for i in range(audio.get_device_count()):
        if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            ic("Input Device id ", i, " - ",
               audio.get_device_info_by_host_api_device_index(0, i).get('name'))
            dev = audio.get_device_info_by_index(i)
            ic((i, dev['name'], dev['maxInputChannels']),
               " Rate : ", dev['defaultSampleRate'])
    ic("-------------------------------------------------------------")


def record_audio_mic(input=1) -> None:

    index = 1
    ic("recording via index "+str(index))

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, input_device_index=index,
                        frames_per_buffer=CHUNK)
    Recordframes = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        Recordframes.append(data)
    ic("recording stopped")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # ic(os.path.join(PATH_FILE,WAVE_OUTPUT_FILENAME))
    wf = wave.open(os.path.join(PATH_FILE, WAVE_OUTPUT_FILENAME), 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(Recordframes))
    wf.close()
    return None


if __name__ == '__main__':
    ic(record_audio_mic())
