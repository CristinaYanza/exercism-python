"""Calculate the score of a dart."""

def score(x, y) -> int:
    """Return the score based on the dart's position."""
    distance = x**2 + y**2

    if distance <= 1:
        return 10 
    if distance <= 25:
        return 5
    if distance <= 100:
        return 1

    return 0