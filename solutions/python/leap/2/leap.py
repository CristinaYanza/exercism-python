def leap_year(year):
    """Returns True if the year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)