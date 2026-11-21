"""Extract rows and columns from a matrix."""


class Matrix:
    """Represent a matrix of numbers."""

    def __init__(self, matrix_string):
        """Convert the matrix string into a list of lists."""

        self.matrix = [
            [int(number) for number in line.split()]
            for line in matrix_string.splitlines()
        ]

    def row(self, index):
        """Return a row from the matrix."""

        return self.matrix[index - 1]

    def column(self, index):
        """Return a column from the matrix."""

        return [
            row[index - 1]
            for row in self.matrix
        ]