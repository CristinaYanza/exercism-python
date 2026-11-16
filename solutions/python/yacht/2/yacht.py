"""Calculate scores for the Yacht dice game."""

# Score categories.
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full house"
FOUR_OF_A_KIND = "four of a kind"
LITTLE_STRAIGHT = "little straight"
BIG_STRAIGHT = "big straight"
CHOICE = "choice"


def score(dice, category):
    """Calculate the score for the selected category."""

    total = sum(dice)

    number_categories = {
        ONES: 1,
        TWOS: 2,
        THREES: 3,
        FOURS: 4,
        FIVES: 5,
        SIXES: 6,
    }

    if category in number_categories:
        value = number_categories[category]
        return dice.count(value) * value

    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0

    if category == FULL_HOUSE:
        counts = sorted(dice.count(value) for value in set(dice))
        return total if counts == [2, 3] else 0

    if category == FOUR_OF_A_KIND:
        for value in set(dice):
            if dice.count(value) >= 4:
                return value * 4
        return 0

    if category in (LITTLE_STRAIGHT, BIG_STRAIGHT):
        straight = (
            {1, 2, 3, 4, 5}
            if category == LITTLE_STRAIGHT
            else {2, 3, 4, 5, 6}
        )
        return 30 if set(dice) == straight else 0

    if category == CHOICE:
        return total

    return 0