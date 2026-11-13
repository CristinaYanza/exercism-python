"""Create a diamond shape using letters."""

def rows(letter):
    """Return a list of strings forming a diamond."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = alphabet.index(letter)
    result = []

    for index in range(position + 1):
        character = alphabet[index]
        outer_spaces = position - index

        if index == 0:
            row = " " * outer_spaces + "A" + " " * outer_spaces
        else:
            inner_spaces = index * 2 - 1
            row = (
                " " * outer_spaces
                + character
                + " " * inner_spaces
                + character
                + " " * outer_spaces
            )

        result.append(row)

    result.extend(result[-2::-1])

    return result