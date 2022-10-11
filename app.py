from audio_utils.recorder import AudioRecorder
from txt_utils.audio_to_text import Text2Audio

ar = AudioRecorder(wave_output_filename="audio.wav")
processes_file = ar.start_recording()
t2a = Text2Audio(processes_file)
text = t2a.transulate()
print(text)
