"""Calculate resistor labels."""

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

def label(colors):
    """Return the resistance value with its metric unit."""

    number = (COLOR_CODES[colors[0]] * 10 + COLOR_CODES[colors[1]]) * 10 ** COLOR_CODES[colors[2]]

    if number >= 1000000000:
        return f"{number / 1000000000:g} gigaohms"

    if number >= 1000000:
        return f"{number / 1000000:g} megaohms"

    if number >= 1000:
        return f"{number / 1000:g} kiloohms"

    return f"{number} ohms"