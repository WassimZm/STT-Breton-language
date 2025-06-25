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
In order to explore the performance of Vosk Model for speech recogniztion, I made 6 evaluation experiences :
### Evaluation With data cleaning :
This represents three evaluation experiences in order to visualize the importance of data cleaning ( the code is taken from Gweltaz code ) :
* **Evaluation on Common Voice dataset**
* **Evaluation on Banque Sonore including dialectal instances**
* **Evaluation on Banque SOnore without taking in concideration dialectal instances ( only standard instances )**
<img src="https://github.com/WassimZm/STT-Breton-language/blob/main/images/Evaluation.jpg" alt="Evaluation results" width="800"/>
