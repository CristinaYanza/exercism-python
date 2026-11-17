"""Find the saddle points in a matrix."""

def saddle_points(matrix):
    """Return the positions of values that are maximum in their row
    and minimum in their column.
    """

    if not matrix:
        return []

    columns = len(matrix[0])

    if any(len(row) != columns for row in matrix):
        raise ValueError("irregular matrix")

    result = []

    for row_index, row in enumerate(matrix):
        row_max = max(row)

        for column_index, value in enumerate(row):
            column = [
                matrix[index][column_index]
                for index in range(len(matrix))
            ]

            if value == row_max and value == min(column):
                result.append({
                    "row": row_index + 1,
                    "column": column_index + 1
                })

    return result