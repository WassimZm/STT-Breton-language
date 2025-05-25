from transcriber import transcribe_audio

import os

import jiwer

import sys


from filter_char import filter_out_chars

from normalizer import normalize_sentence

from utils import pre_process

# Function to evaluate WER and CER for the entire dataset

def evaluate_wer_cer(dataset_path, ground_truth_dict, model):
    wav_files = [f for f in os.listdir(dataset_path) if f.endswith('.wav')]
    wer_scores = []
    cer_scores = []

    for wav_file in wav_files:
        print(f"Processing {wav_file}...")

        # Transcribe the audio file
        transcription = transcribe_audio(os.path.join(dataset_path, wav_file), model)
        if transcription:
            # Load ground truth from the dictionary
            ground_truth = ground_truth_dict.get(wav_file)
            if ground_truth:
                # Compute WER and CER using jiwer 
                PUNCTUATION = '.?!,‚;:«»“”"()[]/…–—•'
                ground_truth = filter_out_chars(ground_truth, PUNCTUATION + '*')
                ground_truth = normalize_sentence(ground_truth, autocorrect=True)
                ground_truth = pre_process(ground_truth).replace('-', ' ').lower()

                
                wer = jiwer.wer(ground_truth, transcription)
                cer = jiwer.cer(ground_truth, transcription)
                wer_scores.append(wer)
                cer_scores.append(cer)
                print(f"WER for {wav_file}: {wer}")
                print(f"CER for {wav_file}: {cer}")
            else:
                print(f"Ground truth not found for {wav_file}.")
        else:
            print(f"Skipping {wav_file} due to transcription failure.")

    # Compute the average WER adn CER for the dataset
    if wer_scores:
        avg_wer = sum(wer_scores) / len(wer_scores)
        avg_cer = sum(cer_scores) / len(cer_scores)
        print(f"Average WER for the dataset: {avg_wer}")
        print(f"Average CER for the dataset: {avg_cer}")
    else:
        print("No WER and CER scores to evaluate.")
