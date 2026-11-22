"""Manage a list of high scores."""


class HighScores:
    """Represent a player's high scores."""

    def __init__(self, scores):
        """Initialize the list of scores."""

        self.scores = scores

    def latest(self):
        """Return the most recent score."""

        return self.scores[-1]

    def personal_best(self):
        """Return the highest score."""

        return max(self.scores)

    def personal_top_three(self):
        """Return the three highest scores."""

        return sorted(self.scores, reverse=True)[:3]