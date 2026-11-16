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

    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0

    if category == ONES:
        return dice.count(1)

    if category == TWOS:
        return dice.count(2) * 2

    if category == THREES:
        return dice.count(3) * 3

    if category == FOURS:
        return dice.count(4) * 4

    if category == FIVES:
        return dice.count(5) * 5

    if category == SIXES:
        return dice.count(6) * 6

    if category == FULL_HOUSE:
        counts = sorted(dice.count(value) for value in set(dice))
        return total if counts == [2, 3] else 0

    if category == FOUR_OF_A_KIND:
        for value in set(dice):
            if dice.count(value) >= 4:
                return value * 4
        return 0

    if category == LITTLE_STRAIGHT:
        return 30 if set(dice) == {1, 2, 3, 4, 5} else 0

    if category == BIG_STRAIGHT:
        return 30 if set(dice) == {2, 3, 4, 5, 6} else 0

    if category == CHOICE:
        return total

    return 0