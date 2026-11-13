"""Determine the relationship between two lists."""

# Possible sublist categories.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"

def sublist(list_one, list_two):
    """Return the relationship between two lists."""

    if list_one == list_two:
        return EQUAL

    if len(list_one) < len(list_two):
        smaller = list_one
        larger = list_two
        result = SUBLIST
    else:
        smaller = list_two
        larger = list_one
        result = SUPERLIST

    if not smaller:
        return result

    for index in range(len(larger) - len(smaller) + 1):
        if larger[index:index + len(smaller)] == smaller:
            return result

    return UNEQUAL