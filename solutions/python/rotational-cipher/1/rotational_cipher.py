"""Rotate letters in a text using a Caesar cipher."""

def rotate(text, key):
    """Return the text with its letters rotated by the given key."""

    result = ""

    for letter in text:
        if letter.isalpha():
            start = ord("A") if letter.isupper() else ord("a")
            new_letter = chr((ord(letter) - start + key) % 26 + start)
            result += new_letter
        else:
            result += letter

    return result