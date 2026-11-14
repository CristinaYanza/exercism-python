"""Generate verses of The Twelve Days of Christmas."""

def recite(start_verse, end_verse):
    """Return the requested verses of the Christmas song."""

    days = [
        "first", "second", "third", "fourth",
        "fifth", "sixth", "seventh", "eighth",
        "ninth", "tenth", "eleventh", "twelfth"
    ]

    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, and a Partridge in a Pear Tree.",
        "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
    ]

    verses = []

    for verse in range(start_verse - 1, end_verse):
        line = (
            f"On the {days[verse]} day of Christmas my true love gave to me: "
            f"{gifts[verse]}"
        )
        verses.append(line)

    return verses