import pyaudio
import wave
import os
from song_recognition.config.settings import sAudiosettings, sPaths, sAPIKeys
from song_recognition.core.exceptions import AudioRecordingError
from icecream import ic


class AudioRecorder:
    """Handles audio recording from microphone"""

    @staticmethod
    def list_input_devices():
        """List available input audio devices"""
        audio = pyaudio.PyAudio()
        devices = []

        for i in range(audio.get_device_count()):
            device_info = audio.get_device_info_by_index(i)
            if device_info['maxInputChannels'] > 0:
                devices.append({
                    'id': i,
                    'name': device_info['name'],
                    'channels': device_info['maxInputChannels']
                })

        return devices

    @classmethod
    def record(cls, duration=None, device_index=1):
        """Record audio from microphone"""
        duration = duration or sAudiosettings.RECORD_SECONDS
        output_path = os.path.join(
            sPaths.DATA_DIR, sAudiosettings.WAVE_OUTPUT_FILENAME)

        try:
            audio = pyaudio.PyAudio()
            stream = audio.open(
                format=sAudiosettings.FORMAT,
                channels=sAudiosettings.CHANNELS,
                rate=sAudiosettings.RATE,
                input=True,
                input_device_index=device_index,
                frames_per_buffer=sAudiosettings.CHUNK
            )

            frames = []
            for _ in range(0, int(sAudiosettings.RATE / sAudiosettings.CHUNK * duration)):
                data = stream.read(sAudiosettings.CHUNK)
                frames.append(data)

            stream.stop_stream()
            stream.close()
            audio.terminate()

            with wave.open(output_path, 'wb') as wf:
                wf.setnchannels(sAudiosettings.CHANNELS)
                wf.setsampwidth(audio.get_sample_size(sAudiosettings.FORMAT))
                wf.setframerate(sAudiosettings.RATE)
                wf.writeframes(b''.join(frames))

            return output_path

        except Exception as e:
            raise AudioRecordingError(f"Failed to record audio: {e}")


if __name__ == '__main__':
    ic(AudioRecorder.record())
