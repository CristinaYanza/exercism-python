"""Determine which plants belong to each kindergarten student."""


class Garden:
    """Represent a kindergarten garden."""

    def __init__(self, diagram, students=None):
        """Initialize the garden and sort the student names."""

        if students is None:
            students = [
                "Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"
            ]

        self.students = sorted(students)

        rows = diagram.splitlines()
        self.first_row = rows[0]
        self.second_row = rows[1]

        self.plant_names = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }

    def plants(self, student):
        """Return the four plants assigned to a student."""

        student_index = self.students.index(student)
        start = student_index * 2
        end = start + 2

        plant_codes = (
            self.first_row[start:end]
            + self.second_row[start:end]
        )

        return [
            self.plant_names[code]
            for code in plant_codes
        ]

    def students_list(self):
        """Return the sorted list of students."""

        return self.students.copy()