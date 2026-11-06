"""Functions for classifying triangles."""

def valid(sides):
    """Check whether the side lengths form a valid triangle."""
    a, b, c = sides
    return min(sides) > 0 and a + b >= c and a + c >= b and b + c >= a

def equilateral(sides):
    """Return True if all three sides are equal."""
    return valid(sides) and sides[0] == sides[1] == sides[2]

def isosceles(sides):
    """Return True if at least two sides are equal."""
    a, b, c = sides
    return valid(sides) and (a == b or a == c or b == c)

def scalene(sides):
    """Return True if all three sides are different."""
    a, b, c = sides
    return valid(sides) and a != b and a != c and b != c