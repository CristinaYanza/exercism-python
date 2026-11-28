class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        allergies = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128
        }

        if item not in allergies:
            return False

        return bool(self.score & allergies[item])

    @property
    def lst(self):
        allergies = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128
        }

        return [
            item
            for item, value in allergies.items()
            if self.score & value
        ]