
* Gweltaz provided a script for noise adding in order to augment the data / model performance.
* **Tdnn:** a type of neural network designed specifically for processing temporal data like audio or speech.
* Kaldi latest version is 5.5.636 7a50987e7 **2020-02-08** [source](https://kaldi-asr.org/doc/versions.html)
## Fine-tuning a vosk model
Anaouder is a vosk model based on **Kaldi** : a framework written in C++ for **building STT models**, it provides tools for **training** and **evaluating** models.
* To train or fine-tune a Vosk model ( like Anaouder ) on additional data, the use of Kaldi is essential, as Vosk relies on models built using Kaldi’s toolkit.
* The Kaldi model used in Vosk is compiled from 3 data sources: [source](https://alphacephei.com/vosk/adaptation)
  - dictionary
  - acoustic model
  - language model
## Evaluating a vosk model
### Using Kaldi commands
steps for evaluating latest model of Speech-to-text :
* Download Kaldi
* Download the latest Vosk model for STT in Breton
* Download the dataset ( it includes audio files and their transcription )
* Generating utt2spk and spk2utt files
* Converting audio files to wav format
* Converting audio files from 4400kHZ to 1600kHZ
* Preparing necessary scripts for the evaluation
* **XXX In Kaldi, features extraction is obliged ( computing MFCC ) XXX**
* Decoding the model
* Evaluating the model
### Using Python
In python it's simpler, I had just to :
* Load the dataset
* Building a copy of dataset with an audio files of 16kHZ
* loading the model
* Inisialization the recognizer with the model
* Evaluating the model based on **WER** and **CER**
## Other notes
**WAV format:** is a standard digital audio file format developed by Microsoft and IBM. It is the best way for Kaldi because it standarize audio formats and it is compatible with Kaldi tools.
