# from .definitions import LETTERS, PUNCTUATION

def filter_out_chars(text: str, chars: str) -> str:
    """ Remove given characters from a string """

    filtered_text = ""
    for l in text:
        if not l in chars: filtered_text += l
    return filtered_text
