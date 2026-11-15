"""Clean and validate phone numbers."""


class PhoneNumber:
    """Represent a valid North American phone number."""

    def __init__(self, number):
        """Initialize and validate the phone number."""

        if any(character.isalpha() for character in number):
            raise ValueError("letters not permitted")

        allowed_characters = set("0123456789 +-().")
        if any(character not in allowed_characters for character in number):
            raise ValueError("punctuations not permitted")

        digits = "".join(
            character for character in number if character.isdigit()
        )

        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")

        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")

        if len(digits) == 11:
            if not digits.startswith("1"):
                raise ValueError("11 digits must start with 1")
            digits = digits[1:]

        if digits[0] == "0":
            raise ValueError("area code cannot start with zero")

        if digits[0] == "1":
            raise ValueError("area code cannot start with one")

        if digits[3] == "0":
            raise ValueError("exchange code cannot start with zero")

        if digits[3] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = digits
        self.area_code = digits[:3]

    def pretty(self):
        """Return the formatted phone number."""

        return (
            f"({self.area_code})-"
            f"{self.number[3:6]}-{self.number[6:]}"
        )