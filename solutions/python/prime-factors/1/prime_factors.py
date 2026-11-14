"""Calculate the prime factors of a number."""

def factors(value):
    """Return the prime factors of the given number."""
    result = []
    divisor = 2

    while value > 1:
        if value % divisor == 0:
            result.append(divisor)
            value //= divisor
        else:
            divisor += 1

    return result