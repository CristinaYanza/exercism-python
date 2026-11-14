"""Encode and decode strings using run-length encoding."""

def decode(string):
    """Decode a run-length encoded string."""
    result = ""
    count = ""

    for character in string:
        if character.isdigit():
            count += character
        else:
            repetitions = int(count) if count else 1
            result += character * repetitions
            count = ""

    return result

def encode(string):
    """Encode a string using run-length encoding."""
    if not string:
        return ""

    result = ""
    count = 1

    for index in range(1, len(string)):
        if string[index] == string[index - 1]:
            count += 1
        else:
            if count > 1:
                result += str(count)

            result += string[index - 1]
            count = 1

    if count > 1:
        result += str(count)

    result += string[-1]

    return result