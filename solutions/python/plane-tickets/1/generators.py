"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""
    letters = "ABCD"
    for i in range(number):
        yield letters[i % 4]

def generate_seats(number):
    """Generate a series of identifiers for airline seats."""
    row = 1
    letters = generate_seat_letters(number)

    for letter in letters:
        if row == 13:
            row += 1
        yield str(row) + letter

        if letter == "D":
            row += 1

def assign_seats(passengers):
    """Assign seats to passengers."""
    seats = generate_seats(len(passengers))
    return dict(zip(passengers, seats))

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket."""
    for seat in seat_numbers:
        code = seat + flight_id
        yield code.ljust(12, "0")