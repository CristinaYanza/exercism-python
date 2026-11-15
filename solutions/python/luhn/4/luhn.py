"""Validate numbers using the Luhn algorithm."""

from dataclasses import dataclass


@dataclass
class Luhn:
    """Validate a number using the Luhn checksum."""

    card_num: str

    def valid(self):
        """Return True if the number passes the Luhn check."""

        number = self.card_num.replace(" ", "")

        if len(number) <= 1 or not number.isdigit():
            return False

        digits = [int(digit) for digit in number]
        digits.reverse()

        total = 0

        for index, digit in enumerate(digits):
            if index % 2 == 1:
                doubled_digit = digit * 2

                if doubled_digit > 9:
                    doubled_digit -= 9

                total += doubled_digit
            else:
                total += digit

        return total % 10 == 0