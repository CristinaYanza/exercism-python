"""Verify whether an ISBN-10 is valid."""

def is_valid(isbn):
    """Return True if the ISBN-10 is valid."""

    isbn = isbn.replace("-", "")

    if len(isbn) != 10 or not isbn[:9].isdigit():
        return False

    if not (isbn[9].isdigit() or isbn[9] == "X"):
        return False

    total = 0

    for i in range(10):
        digit = 10 if isbn[i] == "X" else int(isbn[i])
        total += digit * (10 - i)

    return total % 11 == 0