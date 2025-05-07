
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

