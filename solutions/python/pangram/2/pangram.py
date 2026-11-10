"""Check whether a sentence is a pangram."""

def is_pangram(sentence):
    """Return True if the sentence contains every letter of the alphabet."""

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    return all(letter in sentence.lower() for letter in alphabet)