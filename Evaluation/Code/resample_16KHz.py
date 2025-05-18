
# # Function to resample a WAV file to 16 kHz

def resample_audio(input_path, output_path, target_sample_rate=16000):
    audio = AudioSegment.from_wav(input_path)  # Load the audio file
    audio = audio.set_frame_rate(target_sample_rate)  # Resample the audio
    audio.export(output_path, format="wav")  # Export the resampled audio to a new file

    os.makedirs(output_path, exist_ok=True)

    for file_name in os.listdir(dataset_path):
     if file_name.endswith('.wav'):
        input_file_path = os.path.join(dataset_path, file_name)
        output_file_path = os.path.join(output_path, file_name)
        
        # Resample and save the new file
        print(f"Resampling {input_file_path}...")
        resample_audio(input_file_path, output_file_path)
    print("Resampling complete!")    
