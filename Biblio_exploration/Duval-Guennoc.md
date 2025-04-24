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

## Anaouder project structure
### Supporting Files
#### setup.py
* Defines Metadata, configuration and distribution of project
package.
* It defines command-line tools that users can type while using the
model.
* Setup function, whic is the function that python reads while
installing the project, it
