import csv

def load_ground_truth_dict_commonvoice(tsv_file):
    ground_truth_dict = {}
    with open(tsv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            filename = row['path']  # e.g., 'common_voice_br_18382821.mp3'
            transcription = row['sentence'].strip()
            ground_truth_dict[filename] = transcription
    return ground_truth_dict
