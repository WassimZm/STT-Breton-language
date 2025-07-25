# Kaldi : an Open-Source Toolkit for Speech recognition
Kaldi is a complex **low-level** toolkit that offers a collection of tools such as : audio processing and feature extraction. It provides the core algorithm to build speech-to-text systems from scratch.
* Kaldi supports **TDNN architecture** : a type of neural network designed specifically for processing temporal data like audio or speech.
## Gweltaz Vosk Models:
* Gweltaz has trained several Vosk speech recognition models using **Kaldi**. The most recent model is:
  - **Name** : "vosk-model-br-25.02" ,
  - **Version** : 10 ,
  - **Type** : Vosk ,
  - **URL** : "https://github.com/gweltou/patromou/raw/refs/heads/main/vosk-model-br-25.02.zip".

* Model Training Summary :
  - **Acoustic model** : Time-Delay Neural Network (TDNN)
  - **Number of parameters:** ~5.5 million
  - **Architecture:** 13 hidden layers, each with 786 units
  - **Learning rate:** decayed linearly from 1e-3 to 1e-4
  - **Training duration:** 30 epochs
