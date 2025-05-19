import os
from pydub import AudioSegment

def convert_all_mp3_to_wav(source_folder, destination_folder):
    # Ensure destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Process all mp3 files
    for filename in os.listdir(source_folder):
        if filename.endswith(".mp3"):
            mp3_path = os.path.join(source_folder, filename)
            wav_filename = os.path.splitext(filename)[0] + ".wav"
            wav_path = os.path.join(destination_folder, wav_filename)

            # Load and convert
            audio = AudioSegment.from_mp3(mp3_path)
            audio = audio.set_channels(1).set_frame_rate(16000)
            audio.export(wav_path, format="wav")

            print(f"Converted: {filename} → {wav_filename}")