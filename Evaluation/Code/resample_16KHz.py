from pydub import AudioSegment
import os

# Function to resample a WAV file to 16 kHz
def resample_audio(input_path, output_path, target_sample_rate=16000):
    audio = AudioSegment.from_wav(input_path)  # Load the audio file
    audio = audio.set_frame_rate(target_sample_rate)  # Resample the audio
    audio.export(output_path, format="wav")  # Export the resampled audio to a new file
