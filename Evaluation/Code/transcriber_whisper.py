import wave
import json
import whisper

# Function to process a single audio file and return the transcription

def transcribe_audio(wav_file, model):
    try:
        print(f"Transcribing {wav_file}...")
        result = model.transcribe(wav_file,language="br", verbose=True)
        return result["text"]
    except Exception as e:
        raise e
        print(f"Error transcribing {wav_file}: {e}")
        return None
