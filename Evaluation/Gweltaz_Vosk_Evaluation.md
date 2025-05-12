# Evaluation du modéle "vosk-model-br-25.02" 
## Evaluation on "Banque Sonore des Dialectes Bretons"
### Process of evaluation using python
* Installing the Vosk library using `pip`.
* Downloading and Loading the dataset (https://huggingface.co/datasets/Bretagne/Banque_Sonore_Dialectes_Bretons)
* Building a copy of dataset with an audio files of 16kHZ.
* loading the model.
* Inisialization the recognizer with the model.
* Evaluating the model based on WER and CER.

### Results
* **WER** = 86%
* **CER** = 50%
