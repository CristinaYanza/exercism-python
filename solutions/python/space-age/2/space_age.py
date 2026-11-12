"""Calculate a person's age on different planets."""

class SpaceAge:
    """Calculate age on different planets."""

    def __init__(self, seconds):
        """Initialize the age in seconds."""
        self.seconds = seconds

    def on_earth(self):
        """Return age in Earth years."""
        return round(self.seconds / 31557600, 2)

    def on_mercury(self):
        """Return age in Mercury years."""
        return round(self.seconds / (31557600 * 0.2408467), 2)

    def on_venus(self):
        """Return age in Venus years."""
        return round(self.seconds / (31557600 * 0.61519726), 2)

    def on_mars(self):
        """Return age in Mars years."""
        return round(self.seconds / (31557600 * 1.8808158), 2)

    def on_jupiter(self):
        """Return age in Jupiter years."""
        return round(self.seconds / (31557600 * 11.862615), 2)

    def on_saturn(self):
        """Return age in Saturn years."""
        return round(self.seconds / (31557600 * 29.447498), 2)

    def on_uranus(self):
        """Return age in Uranus years."""
        return round(self.seconds / (31557600 * 84.016846), 2)

    def on_neptune(self):
        """Return age in Neptune years."""
        return round(self.seconds / (31557600 * 164.79132), 2)