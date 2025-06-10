# Evaluation du modéle "vosk-model-br-25.02" 
## Evaluation on "Banque Sonore des Dialectes Bretons"
### Process of evaluation using python
* Installing the Vosk library using `pip`.
     ```bash
   pip install vosk
* Downloading and Loading Common Voice & La banque sonore des Dialectes Bretonnes datasets (https://huggingface.co/datasets/Bretagne/Banque_Sonore_Dialectes_Bretons)
* Preparing a copy of the dataset by converting all audio files to wav format and 16 kHz using the functions `Code/MP3toWAV.py/convert_all_mp3_to_wav` and `Code/resample_16KHz.py/resample_audio`
* Loading the vosk model and initialization the recognizer with the loaded model.
* Dataset instances simplification ( Normalization and Preprocessing the text before evaluation ).
* Evaluating the model based on WER and CER.

### Results

