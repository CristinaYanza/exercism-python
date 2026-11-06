"""Determine whether a number is an Armstrong number."""

def is_armstrong_number(number):
    """Check if a number is equal to the sum of its digits raised to the digit count."""
    digits = str(number)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)

    return total == number