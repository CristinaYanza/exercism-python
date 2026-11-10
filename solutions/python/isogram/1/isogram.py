"""Check whether a phrase is an isogram."""

def is_isogram(phrase):
    """Return True if no letter is repeated."""

    letters = [letter.lower() for letter in phrase if letter.isalpha()]

    return len(letters) == len(set(letters))