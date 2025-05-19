
# this function can change depending on the dataset structure. This one is made for Banque sonores des dialectes bretons

# Read the ground truth file into a dictionary
def load_ground_truth_dict(ground_truth_file):
    ground_truth_dict = {}
    with open(ground_truth_file, 'r') as f:
        for line in f:
            parts = line.strip().split(' ', 1)  # Split into filename and transcription
            if len(parts) == 2:
                filename, transcription = parts
                ground_truth_dict[filename] = transcription
    return ground_truth_dict