# What is Wav2Vec 2.0?
Wav2Vec is a self-supervised learning model for automatic speech recognition (ASR). It was developed and introduced by Facebook AI in 2019 with the paper ”Wav2Vec 2.0: A Framework for Self-Supervised Learning of Speech Representations”.
The model is trained to predict masked portions of the audio while simultaneously learning meaningful speech representations, allowing the model to effectively capture the structure and patterns of spoken language. With just 10 minutes of transcribed speech and 53K hours of unlabeled speech, wav2vec 2.0 enables speech recognition models at a word error rate (WER).

# Wav2Vec 2.0 for Breton language
There exist multilingual pre-trained Wav2Vec 2.0 (XLSR) models, such as XLSR-53, which utilize a large architecture trained on approximately 56,000 hours of speech spanning 53 languages. The training data includes multiple corpora such as MLS, Common Voice, and BABEL. For Breton specifically, the model was trained only on the Common Voice dataset.
