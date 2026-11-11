"""Calculate the Hamming distance between two strands."""

def distance(strand_a, strand_b):
    """Return the number of differences between two strands."""

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    count = 0

    for position, character in enumerate(strand_a):
        if character != strand_b[position]:
            count += 1

    return count