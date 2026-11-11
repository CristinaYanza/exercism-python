"""Recite the nursery rhyme 'This is the House that Jack Built'."""

def recite(start_verse, end_verse):
    """Return the requested verses of the nursery rhyme."""

    subjects = [
        "the house",
        "the malt",
        "the rat",
        "the cat",
        "the dog",
        "the cow with the crumpled horn",
        "the maiden all forlorn",
        "the man all tattered and torn",
        "the priest all shaven and shorn",
        "the rooster that crowed in the morn",
        "the farmer sowing his corn",
        "the horse and the hound and the horn"
    ]

    actions = [
        "",
        "lay in",
        "ate",
        "killed",
        "worried",
        "tossed",
        "milked",
        "kissed",
        "married",
        "woke",
        "kept",
        "belonged to"
    ]

    result = []

    for verse in range(start_verse, end_verse + 1):
        text = "the house that Jack built."

        for position in range(1, verse):
            text = subjects[position] + " that " + actions[position] + " " + text

        result.append("This is " + text)

    return result