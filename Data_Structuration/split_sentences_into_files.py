import os

def split_sentences_to_files(original_text_file, output_folder):
    """
    Reads a text file, extracts the last element from each line,
    and writes each element to a separate text file in the output folder.
    
    Parameters:
        original_text_file (str): Path to the original text file.
        output_folder (str): Path to the folder where individual text files will be saved.
    """
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    with open(original_text_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for idx, line in enumerate(lines):
        # Strip newline and split by tab or multiple spaces
        parts = line.strip().split()
        if not parts:
            continue
        
        # Take the last element as the sentence
        sentence = parts[-1]
        
        # Handle cases where the sentence might have spaces (if the file uses tabs for splitting)
        # If the last element includes spaces (like a sentence), you may need to join all after the 6th element
        if len(parts) > 7:  
            sentence = ' '.join(parts[7:])
        
        # Create filename
        file_path = os.path.join(output_folder, f"clip_{idx}.txt")
        
        # Write the sentence to file
        with open(file_path, 'w', encoding='utf-8') as out_f:
            out_f.write(sentence)

    print(f"[INFO] {len(lines)} sentences written to {output_folder}")
