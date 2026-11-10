"""Check whether a sentence is a pangram."""

def is_pangram(sentence):
    """Return True if the sentence contains every letter of the alphabet."""

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        if letter not in sentence.lower():
            return False

    return True