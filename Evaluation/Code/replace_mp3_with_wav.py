# Reads the TSV file ( from CommonVoice dataset ) and replaces all occurrences of '.mp3' with '.wav' in the first
# column (audio filename).

import csv

def replace_mp3_with_wav(input_tsv, output_tsv):
    with open(input_tsv, 'r', newline='', encoding='utf-8') as infile, \
         open(output_tsv, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile, delimiter='\t')  # Read TSV with tab delimiter
        fieldnames = reader.fieldnames
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        
        for row in reader:
            # Replace ".mp3" with ".wav" in the 'path' field
            if '.mp3' in row['path']:
                row['path'] = row['path'].replace('.mp3', '.wav')
            writer.writerow(row)

# Example usage
# replace_mp3_with_wav(ground_truth_path, '/home/ouassim/Desktop/stage/Data_Wav_16/test_wav.tsv')
