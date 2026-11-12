"""Calculate the difference between the square of sums and sum of squares."""

def square_of_sum(number):
    """Return the square of the sum of the first natural numbers."""
    total = sum(range(1, number + 1))
    return total ** 2


def sum_of_squares(number):
    """Return the sum of the squares of the first natural numbers."""
    total = sum(current_number ** 2 for current_number in range(1, number + 1))
    return total


def difference_of_squares(number):
    """Return the difference between both calculations."""
    return square_of_sum(number) - sum_of_squares(number)