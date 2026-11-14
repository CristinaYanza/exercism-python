"""Create an acronym from a phrase."""

def abbreviate(words):
    """Return the acronym of the given phrase."""
    words = words.replace("-", " ")
    result = []

    for word in words.split():
        letter = ""

        for character in word:
            if character.isalpha():
                letter = character.upper()
                break

        if letter:
            result.append(letter)

    return "".join(result)