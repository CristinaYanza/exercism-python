"""Transform legacy scoring data into the new format."""

def transform(legacy_data):
    """Convert letters and scores into a letter-to-score dictionary."""
    result = {}

    for score, letters in legacy_data.items():
        for letter in letters:
            result[letter.lower()] = score

    return result