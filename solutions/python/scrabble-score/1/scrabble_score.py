"""Calculate the Scrabble score of a word."""

def score(word):
    """Return the total Scrabble score of a word."""

    letter_values = {
        1: "AEIOULNRST",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ"
    }

    total = 0

    for character in word.upper():
        for points, letters in letter_values.items():
            if character in letters:
                total += points
                break

    return total