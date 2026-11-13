"""Calculate the integer square root of a number."""

def square_root(number):
    """Return the integer square root using binary search."""
    low = 1
    high = number

    while low <= high:
        middle = (low + high) // 2
        square = middle * middle

        if square == number:
            return middle
        if square < number:
            low = middle + 1
        else:
            high = middle - 1

    return None 