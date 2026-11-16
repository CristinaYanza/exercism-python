"""Transpose rows of text into columns."""

def transpose(text):
    """Return the transposed version of the input text."""

    if not text:
        return ""

    rows = text.split("\n")
    max_length = max(len(row) for row in rows)

    result = []

    for column in range(max_length):
        transposed_row = ""

        last_row = max(
            index
            for index, row in enumerate(rows)
            if column < len(row)
        )

        for row_index, row in enumerate(rows[:last_row + 1]):
            if column < len(row):
                transposed_row += row[column]
            else:
                transposed_row += " "

        result.append(transposed_row)

    return "\n".join(result)