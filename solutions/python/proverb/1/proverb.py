"""Generate a proverb from a list of words."""

def proverb(*words, qualifier=None):
    """Return a proverb based on the given words."""

    if not words:
        return []

    result = []

    for index in range(len(words) - 1):
        result.append(
            f"For want of a {words[index]} the {words[index + 1]} was lost."
        )

    final_word = words[0]

    if qualifier:
        final_word = f"{qualifier} {final_word}"

    result.append(f"And all for the want of a {final_word}.")

    return result