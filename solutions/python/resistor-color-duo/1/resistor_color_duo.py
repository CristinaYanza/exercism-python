"""Calculate the value of a resistor from its colors."""

COLOR_CODES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def value(colors):
    """Return the two-digit value of the first two colors."""
    return COLOR_CODES[colors[0]] * 10 + COLOR_CODES[colors[1]]