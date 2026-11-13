"""Check whether brackets are correctly paired."""

def is_paired(input_string):
    """Return True if all brackets are correctly paired."""
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in input_string:
        if character in "([{":
            stack.append(character)

        elif character in ")]}":
            if not stack or stack[-1] != pairs[character]:
                return False

            stack.pop()

    return len(stack) == 0