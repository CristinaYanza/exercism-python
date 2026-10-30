"""Functions to help edit essay homework using string manipulation."""

def capitalize_title(title) -> str:
    """Convert the first letter of each word in the title to uppercase."""
    return title.title()

def check_sentence_ending(sentence):
    """Check if the sentence ends with a period."""
    return sentence.endswith(".")

def clean_up_spacing(sentence):
    """Remove whitespace from the beginning and end."""
    return sentence.strip()

def replace_word_choice(sentence, old_word, new_word):
    """Replace all occurrences of a word with another word."""
    return sentence.replace(old_word, new_word)