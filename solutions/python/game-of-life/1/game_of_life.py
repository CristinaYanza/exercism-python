"""Calculate the next generation in Conway's Game of Life."""

def tick(matrix):
    """Return the next generation of cells."""

    if not matrix:
        return []

    rows = len(matrix)
    columns = len(matrix[0])

    result = []

    for row in range(rows):
        new_row = []

        for column in range(columns):
            neighbors = 0

            for row_offset in (-1, 0, 1):
                for column_offset in (-1, 0, 1):
                    if row_offset == 0 and column_offset == 0:
                        continue

                    neighbor_row = row + row_offset
                    neighbor_column = column + column_offset

                    if (
                        0 <= neighbor_row < rows
                        and 0 <= neighbor_column < columns
                    ):
                        neighbors += matrix[neighbor_row][neighbor_column]

            cell = matrix[row][column]

            if cell == 1 and neighbors in (2, 3):
                new_row.append(1)
            elif cell == 0 and neighbors == 3:
                new_row.append(1)
            else:
                new_row.append(0)

        result.append(new_row)

    return result