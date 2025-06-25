# Evaluation du modéle "vosk-model-br-25.02" 
## Process of evaluation using python
* Installing the Vosk library using `pip`.
     ```bash
   pip install vosk
* Downloading and Loading Common Voice & La banque sonore des Dialectes Bretonnes datasets (https://huggingface.co/datasets/Bretagne/Banque_Sonore_Dialectes_Bretons)
* Preparing a copy of the dataset by converting all audio files to wav format and 16 kHz using the functions `Code/MP3toWAV.py/convert_all_mp3_to_wav` and `Code/resample_16KHz.py/resample_audio`
* Loading the vosk model and initialization the recognizer with the loaded model.
* Dataset instances simplification ( Normalization and Preprocessing the text before evaluation ).
* Evaluating the model based on WER and CER.

<img src="https://github.com/WassimZm/STT-Breton-language/blob/main/images/Data_Cleaning_and_Evaluation.png" alt="Evaluation results" width="800"/>

## Results

To evaluate the performance of the Vosk model for speech recognition, I conducted six evaluation experiments:

### 1. **Without Data Cleaning**
These first three experiments were performed without any data cleaning:
- **Evaluation on the Common Voice dataset**
- **Evaluation on the Banque Sonore dataset, including dialectal instances**
- **Evaluation on the Banque Sonore dataset, excluding dialectal instances (standard Breton only)**

### 2. **With Data Cleaning**
To assess the impact of data cleaning, the same three experiments were repeated using a cleaned version of the data (cleaning script adapted from Gweltaz’s code):
- **Evaluation on the Common Voice dataset**
- **Evaluation on the Banque Sonore dataset, including dialectal instances**
- **Evaluation on the Banque Sonore dataset, excluding dialectal instances (standard Breton only)**

### Summary of Results
The results of all six evaluations are summarized in the table below :
<img src="https://github.com/WassimZm/STT-Breton-language/blob/main/images/Evaluation.jpg" alt="Evaluation results" width="800"/>
