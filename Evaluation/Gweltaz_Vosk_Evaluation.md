# Evaluation du modéle "vosk-model-br-25.02" 
## Evaluation on "Banque Sonore des Dialectes Bretons"
### Process of evaluation using python
* Installing the Vosk library using `pip`.
     ```bash
   pip install vosk
* Downloading and Loading the dataset (https://huggingface.co/datasets/Bretagne/Banque_Sonore_Dialectes_Bretons)
* Preparing a copy of the dataset by converting all audio files to 16 kHz using the function `Code/resample_16KHz.py/resample_audio`
* Loading the vosk model and initialization the recognizer with the loaded model.
* Dataset instances simplification
* Evaluating the model based on WER and CER.

### Results

