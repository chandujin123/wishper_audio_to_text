import pyaudio
import wave
from regex import R
from torch import chunk

class AudioRecorder:
    def __init__(self,chunk=1024,audio_format=pyaudio.paInt16,channels = 2 ,rate=44100,recorded_seconds=5,wave_output_filename="voice.wav"):
        self.chunk =        chunk
        self.audio_format = audio_format
        self.channels =     channels
        self.rate =         rate
        self.recorded_seconds = recorded_seconds
        self.wave_output_filename = wave_output_filename
        
    def start_recording(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=self.audio_format,
                channels=self.channels,
                rate=self.rate,
                input=True,
                frames_per_buffer=self.chunk)
        print("* recording")
        frames = []
        try:
            while True:
                data = stream.read(self.chunk)
                frames.append(data)
        except KeyboardInterrupt:
            print("recording stopped")
        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(self.wave_output_filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(self.audio_format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        return self.wave_output_filename