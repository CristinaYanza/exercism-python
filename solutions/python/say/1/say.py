"""Convert numbers into English words."""

def say(number):
    """Return the number expressed in English words."""

    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    ones = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    ]

    teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    def convert_hundreds(value):
        """Convert a number from 1 to 999 into words."""
        words = []

        if value >= 100:
            words.append(ones[value // 100])
            words.append("hundred")
            value %= 100

        if value >= 20:
            word = tens[value // 10]

            if value % 10 != 0:
                word += "-" + ones[value % 10]

            words.append(word)

        elif value >= 10:
            words.append(teens[value - 10])

        elif value > 0:
            words.append(ones[value])

        return " ".join(words)

    scales = [
        (1000000000, "billion"),
        (1000000, "million"),
        (1000, "thousand"),
        (1, "")
    ]

    result = []

    for value, name in scales:
        group = number // value
        number %= value

        if group > 0:
            words = convert_hundreds(group)
            if name:
                words += " " + name
            result.append(words)

    return " ".join(result)