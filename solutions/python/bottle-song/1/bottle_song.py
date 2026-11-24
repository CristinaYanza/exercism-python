"""Generate the lyrics of the Ten Green Bottles song."""

def recite(start, take=1):
    """Return the requested verses of the song."""

    numbers = {
        0: "no",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten"
    }

    lyrics = []

    for bottles in range(start, start - take, -1):
        current = numbers[bottles]
        next_bottles = numbers[bottles - 1]

        bottle_word = "bottle" if bottles == 1 else "bottles"
        next_word = "bottle" if bottles - 1 == 1 else "bottles"

        lyrics.extend([
            f"{current.capitalize()} green {bottle_word} hanging on the wall,",
            f"{current.capitalize()} green {bottle_word} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {next_bottles} green {next_word} hanging on the wall."
        ])

        if bottles > start - take + 1:
            lyrics.append("")

    return lyrics