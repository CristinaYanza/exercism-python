"""Resistor color codes."""

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


def color_code(color):
    """Return the numeric code of a color."""
    return COLOR_CODES[color]


def colors():
    """Return the list of resistor colors."""
    return list(COLOR_CODES)