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
* **WER** = 86% ( took 1h for evaluation )
* **CER** = 50% ( took 1h and half for evaluation )

* It seems that CER (Character Error Rate) provides a more accurate reflection of the model’s performance, for example:
 - **Correct transcription:** Hervez kont...
 - **Model Transcription:** hervez kont

 - **WER :** 1.0 ( 100% of the words are considered incorrect )
 - **CER :** 0.2857142857142857 ( Only 28% of the characters are incorrect )
