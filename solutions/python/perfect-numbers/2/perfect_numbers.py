"""Classify numbers as perfect, abundant, or deficient."""

def classify(number):
    """Return the classification of a positive integer."""

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    total = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            total += divisor

    if total == number:
        return "perfect"

    if total > number:
        return "abundant"

    return "deficient"