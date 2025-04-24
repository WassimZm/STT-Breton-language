# Duval-Guennoc 2022-present - Anaouder
## Anaouder : a VOSK model for the Breton language.
* It is a toolbox in python available online designed specifically
for Speech-To-Text recognization.
* It was made for generating transcriptions from a video or an audio in Breton
with taking in concideration Capital letters ( for proper nouns )
and number, dates, quantities ... etc.
* The model is trained on 60 hours of Speech, tho it doesn't offer
a very high performance.
## What is Anaouder based on?
Anaouder is a python package based on **Vosk**, a high-level API for speech-to-text, which is itself based on a low-level toolkit called **Kaldi**.
### Vosk
* It is a library that offers the ability of using pre-trained models for speech recognition.
* It supports python and some other programming languages.
### Kaldi
* It is a complex low-level toolkit that offers a collection of tools such as : audio processing and feature extraction.
* It provides the core algorithm to build speech-to-text systems from scratch.

## Anaouder project structure : Supporting Files
#### setup.py :
* Defines Metadata, configuration and distribution of project
package.
* It defines command-line tools that users can type while using the
model.
* Setup function, which is the function that python reads while
installing the project.
#### requirements.txt :
Lists all Python packages and dependencies needed to run the project smoothly.
#### projects_using_vosk.md :
Lists example projects and applications that utilize the Vosk speech recognition model.
#### README.md + README-fr.md :
Provide instructions and details for using the model — in Breton `README.md` and in French `README-fr.md`.
#### LICENSE :
Specifies the terms and conditions under which the project can be used, modified, and shared.
#### CHANGELOG.md :
Documents the history of changes, updates, and versions of the project since its creation.

## Anaouder project structure : Anaouder model
### version.py :
Stores the current version of the project : VERSION = "1.0.3".
### utils.py :
This file provides functions for logging messages with colors, converting time, dropping comments and loading the dataset.
### normalization.py :
* This script is designed to be automatically used after the transcription happens.
* It's main role is to normalize the resulting text from transcription ( removing unwanted characters ... etc ).
### mikro.py :
* This script allows real-time transcription from a microphone.
* It calls the project's main modules for:  
  - Loading ASR model (`load_model`).
  - Normalization and post-processing of the text (`post_process_text`).
  - Sentence tokenization / detokenization (`tokenize` & `detokenize`).
  - Getting Anaouder version (`VERSION`).



