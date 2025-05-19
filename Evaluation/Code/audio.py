import os
from pydub import AudioSegment

def resample_all_wav(source_folder, output_folder, target_sample_rate=16000):
    """
    Resample all WAV files in the source folder to the target sample rate
    and save them in the output folder.

    Args:
        source_folder (str): Path to the folder containing original WAV files.
        output_folder (str): Path to save the resampled WAV files.
        target_sample_rate (int): Desired sample rate (default: 16000 Hz).
    """
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(source_folder):
        if filename.endswith(".wav"):
            input_path = os.path.join(source_folder, filename)
            output_path = os.path.join(output_folder, filename)

            print(f"Resampling {filename} to {target_sample_rate} Hz...")

            audio = AudioSegment.from_wav(input_path)
            audio = audio.set_frame_rate(target_sample_rate)
            audio.export(output_path, format="wav")

    print("✅ All files resampled successfully!")