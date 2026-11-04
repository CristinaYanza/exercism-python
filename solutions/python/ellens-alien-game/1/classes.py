"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Represent an alien in the game."""

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        """Initialize an alien with coordinates and health."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

        Alien.total_aliens_created += 1

    def hit(self):
        """Decrease the alien's health by one."""
        self.health -= 1

    def is_alive(self):
        """Return True if the alien has health remaining."""
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move the alien to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        """Reserve a method for future collision detection."""
        pass


def new_aliens_collection(alien_start_positions):
    """Create a collection of aliens from a list of coordinates."""
    aliens = []

    for position in alien_start_positions:
        alien = Alien(position[0], position[1])
        aliens.append(alien)

    return aliens