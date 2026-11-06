"""Functions for classifying triangles."""

def valid(sides):
    """Check whether the side lengths form a valid triangle."""
    first, second, third = sides
    return (min(sides) > 0 and
            first + second >= third and
            first + third >= second and
            second + third >= first)

def equilateral(sides):
    """Return True if all three sides are equal."""
    return valid(sides) and sides[0] == sides[1] == sides[2]

def isosceles(sides):
    """Return True if at least two sides are equal."""
    first, second, third = sides
    return valid(sides) and (
        first == second or first == third or second == third
    )

def scalene(sides):
    """Return True if all three sides are different."""
    first, second, third = sides
    return valid(sides) and (
        first != second and first != third and second != third
    )