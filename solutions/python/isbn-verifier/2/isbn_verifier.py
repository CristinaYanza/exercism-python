"""Verify whether an ISBN-10 is valid."""

def is_valid(isbn):
    """Return True if the ISBN-10 is valid."""

    isbn = isbn.replace("-", "")

    if len(isbn) != 10 or not isbn[:9].isdigit():
        return False

    if not (isbn[9].isdigit() or isbn[9] == "X"):
        return False

    total = 0

    for position in range(10):
        digit = 10 if isbn[position] == "X" else int(isbn[position])
        total += digit * (10 - position)

    return total % 11 == 0