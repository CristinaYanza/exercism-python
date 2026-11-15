"""Generate a Dungeons & Dragons character."""

import random


def modifier(value):
    """Calculate the ability modifier."""
    return (value - 10) // 2


class Character:
    """Represent a Dungeons & Dragons character."""

    def __init__(self):
        """Generate the character's abilities and hit points."""

        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        """Roll four dice and sum the three highest values."""

        dice_values = [random.randint(1, 6) for _ in range(4)]

        return sum(sorted(dice_values)[1:])