"""Translate text into Pig Latin."""

def translate(text):
    """Translate each word according to Pig Latin rules."""
    vowels = "aeiou"
    translated = []

    for word in text.split():
        if word[0] in vowels or word.startswith(("xr", "yt")):
            translated.append(word + "ay")
            continue

        split_index = len(word)

        for index, letter in enumerate(word):
            if letter in vowels:
                split_index = index
                break

            if word[index:index + 2] == "qu":
                split_index = index + 2
                break

            if letter == "y" and index > 0:
                split_index = index
                break

        translated.append(
            word[split_index:] + word[:split_index] + "ay"
        )

    return " ".join(translated)