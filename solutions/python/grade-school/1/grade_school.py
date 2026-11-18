"""Manage students and their grades in a school."""

class School:
    """Represent a school and its students."""

    def __init__(self):
        """Initialize an empty school."""

        self.students = {}
        self.added_students = []

    def add_student(self, name, grade):
        """Add a student if they are not already enrolled."""

        if any(
            student_name == name
            for students in self.students.values()
            for student_name in students
        ):
            self.added_students.append(False)
            return

        if grade not in self.students:
            self.students[grade] = []

        self.students[grade].append(name)
        self.added_students.append(True)

    def roster(self):
        """Return all students sorted by grade and name."""

        result = []

        for grade_number in sorted(self.students):
            result.extend(sorted(self.students[grade_number]))

        return result

    def grade(self, grade_number):
        """Return students in a specific grade, sorted by name."""

        return sorted(self.students.get(grade_number, []))

    def added(self):
        """Return the results of all student additions."""

        return self.added_students