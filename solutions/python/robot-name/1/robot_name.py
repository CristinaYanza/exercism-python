"""Manage randomly generated robot names."""

import random
import string


class Robot:
    """Represent a robot with a unique random name."""

    used_names = set()

    def __init__(self):
        """Initialize a robot without a name."""
        self._name = None
        self._previous_name = None

    @property
    def name(self):
        """Return the robot's name, generating one if necessary."""
        if self._name is None:
            while True:
                letters = ''.join(
                    random.choices(string.ascii_uppercase, k=2)
                )
                digits = ''.join(
                    random.choices(string.digits, k=3)
                )
                new_name = letters + digits

                if (
                    new_name not in Robot.used_names
                    and new_name != self._previous_name
                ):
                    Robot.used_names.add(new_name)
                    self._name = new_name
                    break

        return self._name

    def reset(self):
        """Reset the robot and release its current name."""
        if self._name is not None:
            self._previous_name = self._name
            Robot.used_names.remove(self._name)
            self._name = None