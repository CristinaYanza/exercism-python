"""Find anagrams of a given word."""

def find_anagrams(word, candidates):
    """Return the candidates that are anagrams of the given word."""

    result = []

    for candidate in candidates:
        if candidate.lower() != word.lower():
            if sorted(candidate.lower()) == sorted(word.lower()):
                result.append(candidate)

    return result