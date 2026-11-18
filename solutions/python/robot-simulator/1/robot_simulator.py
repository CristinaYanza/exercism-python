"""Simulate a robot moving on a two-dimensional grid."""

# Directions
EAST = "east"
NORTH = "north"
WEST = "west"
SOUTH = "south"


class Robot:
    """Represent a robot that can move and rotate."""

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        """Initialize the robot's direction and coordinates."""

        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions):
        """Execute a sequence of movement instructions."""

        directions = [NORTH, EAST, SOUTH, WEST]
        movements = {
            NORTH: (0, 1),
            EAST: (1, 0),
            SOUTH: (0, -1),
            WEST: (-1, 0),
        }

        for instruction in instructions:
            if instruction == "R":
                index = directions.index(self.direction)
                self.direction = directions[(index + 1) % 4]

            elif instruction == "L":
                index = directions.index(self.direction)
                self.direction = directions[(index - 1) % 4]

            elif instruction == "A":
                x, y = self.coordinates
                dx, dy = movements[self.direction]

                self.coordinates = (x + dx, y + dy)