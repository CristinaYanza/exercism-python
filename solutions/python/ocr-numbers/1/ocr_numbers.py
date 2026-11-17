"""Convert OCR representations of digits into numbers."""

DIGITS = {
    (" _ ", "| |", "|_|", "   "): "0",
    ("   ", "  |", "  |", "   "): "1",
    (" _ ", " _|", "|_ ", "   "): "2",
    (" _ ", " _|", " _|", "   "): "3",
    ("   ", "|_|", "  |", "   "): "4",
    (" _ ", "|_ ", " _|", "   "): "5",
    (" _ ", "|_ ", "|_|", "   "): "6",
    (" _ ", "  |", "  |", "   "): "7",
    (" _ ", "|_|", "|_|", "   "): "8",
    (" _ ", "|_|", " _|", "   "): "9",
}


def convert(input_grid):
    """Convert a grid of OCR characters into a string of digits."""

    if len(input_grid) % 4 != 0:
        raise ValueError(
            "Number of input lines is not a multiple of four"
        )

    if input_grid and len(input_grid[0]) % 3 != 0:
        raise ValueError(
            "Number of input columns is not a multiple of three"
        )

    if not input_grid:
        return ""

    columns = len(input_grid[0])

    if any(len(row) != columns for row in input_grid):
        raise ValueError(
            "Number of input columns is not a multiple of three"
        )

    result = []

    for start_row in range(0, len(input_grid), 4):
        number = ""

        for start_column in range(0, columns, 3):
            cell = tuple(
                input_grid[row][start_column:start_column + 3]
                for row in range(start_row, start_row + 4)
            )

            number += DIGITS.get(cell, "?")

        result.append(number)

    return ",".join(result)