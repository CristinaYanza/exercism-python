"""Find Pythagorean triplets with a given sum."""

def triplets_with_sum(number):
    """Return all Pythagorean triplets whose sum equals number."""

    triplets = []

    for a in range(1, number // 3):
        for b in range(a + 1, (number - a + 1) // 2):
            c = number - a - b

            if a * a + b * b == c * c:
                triplets.append([a, b, c])

    return triplets