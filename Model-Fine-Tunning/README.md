# Fine Tunning Whisper steps :

## DATA PREPARATION :

**def clean_text(text: str) -> str:**
- Cleaning transcription text
- It can be replaced by cleaning code that Gweltaz provided


**class WhisperStreamingDataset(IterableDataset):**
- Handles large datasets, make it easy to preprocess big data
- def __init__(self, hf_dataset, feature_extractor, tokenizer):
   def __iter__(self):
   
**def load_and_preprocess_data**(path,language=None, use_huggingface=False,token=None ,feature_extractor=None, tokenizer=None):
 - Prepares data from a given source (Hugging Face / a local folder) : generating audio features + and converting transcriptions into tokenized form.

 - def audio_text_generator(data_dir):
    - Takes as an input a folder ( data_dir ), the folder should contain wav files for each instance + text files that contain
    the transcription of each audio file.
   - pairing audio and transcription by generating a dictionnary
     - {
         "audio": "/path/to/data_dir/sample1.wav",
         "sentence": "This is the transcription of the audio file."
       }
      
 - def prepare_dataset(batch, feature_extractor, tokenizer):
    - Prepares a batch of Audio and Text data to be used by a model ( training task ).
    - Extracting audio features and stores the results in a vector
    - Tokenizing the transcription text and makes a numerical representation.2
    
 - Loading and splitting the dataset and apply all the preprocessing steps
 
## MODEL PREPARATION:
- Loading Whisper model
- Define the model's task ( transcription ) and language ( Breton ).
- Feature extraction : Extractor
- Tokenization : Tokenizer

## COLLATOR FOR BATCHING:
- Standarizing data vectors ( audio and text ) => making all vectors with a similar length

## FINE-TUNNING LOGIC FOR WHISPER:
- using "def forward", "def training_step" and "def validation_step"  => Computing loss, updating parameters and checking
performance.
- Loading train and validation data + Optimizer + generate predictions

## TRAINER:
- Initializing a trainer : Using EarlyStopping + Measuring training time + Saving the best model ...
- Generate transcriptions (predictions) for a dataset using a trained Whisper model and compare them with reference texts
