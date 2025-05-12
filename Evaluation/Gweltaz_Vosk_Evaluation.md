# Evaluation du modéle "vosk-model-br-25.02" 
## Evaluation on "Banque Sonore des Dialectes Bretons"
### Process of evaluation using python
* Installing the Vosk library using `pip`.
     ```bash
   pip install vosk
* Downloading and Loading the dataset (https://huggingface.co/datasets/Bretagne/Banque_Sonore_Dialectes_Bretons)
* Preparing a copy of the dataset by converting all audio files to 16 kHz.
* Loading the vosk model.
* Initialization the recognizer with the loaded model.
* Evaluating the model based on WER and CER.

### Results
* **WER** = 86%
* **CER** = 50%
