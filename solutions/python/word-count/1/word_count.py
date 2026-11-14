"""Count the occurrences of each word in a sentence."""

def count_words(sentence):
    """Return a dictionary with the frequency of each word."""

    words = sentence.lower().split()
    result = {}

    for word in words:
        clean_word = ""

        for index, character in enumerate(word):
            if character.isalnum():
                clean_word += character

            elif character == "'":
                if (
                    index > 0
                    and index < len(word) - 1
                    and word[index - 1].isalnum()
                    and word[index + 1].isalnum()
                ):
                    clean_word += character
                else:
                    clean_word += " "

            else:
                clean_word += " "

        for part in clean_word.split():
            result[part] = result.get(part, 0) + 1

    return result