"""Encode and decode text using the Atbash cipher."""

def encode(plain_text):
    """Encode text and group the result into blocks of five."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = alphabet[::-1]
    translation = str.maketrans(alphabet, reversed_alphabet)

    result = ""

    for character in plain_text.lower():
        if character.isalnum():
            result += character.translate(translation)

    groups = []

    for index in range(0, len(result), 5):
        groups.append(result[index:index + 5])

    return " ".join(groups)

def decode(ciphered_text):
    """Decode text using the Atbash cipher."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = alphabet[::-1]
    translation = str.maketrans(reversed_alphabet, alphabet)

    result = ""

    for character in ciphered_text.lower():
        if character.isalnum():
            result += character.translate(translation)

    return result