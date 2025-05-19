from vosk import Model, KaldiRecognizer
import wave
import json

# Function to process a single audio file and return the transcription

def transcribe_audio(wav_file, model):
    # Open the WAV file
    wf = wave.open(wav_file, "rb")
    
    # Check if the WAV file has the correct sample rate (16 kHz)
    if wf.getframerate() != 16000:
        print(f"Warning: {wav_file} has incorrect sample rate ({wf.getframerate()}). Skipping.")
        return None
    
    # Initialize the recognizer with the model
    recognizer = KaldiRecognizer(model, wf.getframerate())
    
    # Recognize speech from the audio
    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            results.append(json.loads(recognizer.Result()))
    
    # Finalize the recognition process
    results.append(json.loads(recognizer.FinalResult()))
    
    # Extract the recognized text from the results
    recognized_text = " ".join([result['text'] for result in results if 'text' in result])
    
    return recognized_text