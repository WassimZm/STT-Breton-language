# Evaluation du modéle "vosk-model-br-25.02" 
## Evaluation on "Banque Sonore des Dialectes Bretons"
### Process of evaluation using python
* Installing the Vosk library using `pip`.
     ```bash
   pip install vosk
* Downloading and Loading the dataset (https://huggingface.co/datasets/Bretagne/Banque_Sonore_Dialectes_Bretons)
* Preparing a copy of the dataset by converting all audio files to 16 kHz.
  ```python
  from pydub import AudioSegment
import os

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
* Loading the vosk model.
* Initialization the recognizer with the loaded model.
* Evaluating the model based on WER and CER.

### Results
* **WER** = 86%
* **CER** = 50%
