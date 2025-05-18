import os
from pydub import AudioSegment

def resample_audio(input_path, output_path, target_sample_rate=16000):
    """Resample a single WAV audio file."""
    audio = AudioSegment.from_wav(input_path)
    audio = audio.set_frame_rate(target_sample_rate)
    audio.export(output_path, format="wav")

# Folder-level logic (outside the function)
def resample_folder(dataset_path, output_folder, target_sample_rate=16000):
    """Apply resampling to all WAV files in a folder."""
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(dataset_path):
        if file_name.endswith('.wav'):
            input_file_path = os.path.join(dataset_path, file_name)
            output_file_path = os.path.join(output_folder, file_name)

            print(f"Resampling {input_file_path}...")
            resample_audio(input_file_path, output_file_path, target_sample_rate)

    print("Resampling complete!")
 
