

from transcriber import transcribe_audio

import os

import jiwer

# Function to evaluate WER for the entire dataset

def evaluate_wer(dataset_path, ground_truth_dict, model):
    wav_files = [f for f in os.listdir(dataset_path) if f.endswith('.wav')]
    wer_scores = []

    for wav_file in wav_files:
        print(f"Processing {wav_file}...")

        # Transcribe the audio file
        transcription = transcribe_audio(os.path.join(dataset_path, wav_file), model)
        if transcription:
            # Load ground truth from the dictionary
            ground_truth = ground_truth_dict.get(wav_file)
            if ground_truth:
                # Compute WER using jiwer
                wer = jiwer.wer(ground_truth, transcription)
                wer_scores.append(wer)
                print(f"WER for {wav_file}: {wer}")
            else:
                print(f"Ground truth not found for {wav_file}.")
        else:
            print(f"Skipping {wav_file} due to transcription failure.")

    # Compute the average WER for the dataset
    if wer_scores:
        avg_wer = sum(wer_scores) / len(wer_scores)
        print(f"Average WER for the dataset: {avg_wer}")
    else:
        print("No WER scores to evaluate.")
