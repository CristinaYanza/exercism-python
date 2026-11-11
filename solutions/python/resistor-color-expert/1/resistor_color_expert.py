"""Calculate resistor values and tolerances."""

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

TOLERANCES = {
    "grey": "0.05",
    "violet": "0.1",
    "blue": "0.25",
    "green": "0.5",
    "brown": "1",
    "red": "2",
    "gold": "5",
    "silver": "10"
}

def resistor_label(colors):
    """Return the resistance value and tolerance."""

    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        digits = colors[:2]
        multiplier = colors[2]
    else:
        digits = colors[:3]
        multiplier = colors[3]

    number = 0

    for color in digits:
        number = number * 10 + COLOR_CODES[color]

    number *= 10 ** COLOR_CODES[multiplier]

    tolerance = TOLERANCES[colors[-1]]

    if number >= 1000000:
        number /= 1000000
        unit = "megaohms"
    elif number >= 1000:
        number /= 1000
        unit = "kiloohms"
    else:
        unit = "ohms"

    return f"{number:g} {unit} ±{tolerance}%"