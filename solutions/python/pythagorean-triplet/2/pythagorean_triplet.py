"""Find Pythagorean triplets with a given sum."""

def triplets_with_sum(number):
    """Return all Pythagorean triplets whose sum equals number."""

    triplets = []

    for first_number in range(1, number // 3):
        for second_number in range(
            first_number + 1,
            (number - first_number + 1) // 2
        ):
            third_number = number - first_number - second_number

            if (
                first_number ** 2 + second_number ** 2
                == third_number ** 2
            ):
                triplets.append([
                    first_number,
                    second_number,
                    third_number
                ])

    return triplets