"""File to define Bear class."""

__author__: str = "730557969"


class Bear:
    """Creating a New Class called Bear!"""

    age: int  # attributes of Bear.
    hunger_score: int

    def __init__(self):
        """Initialzing a Bear class object!"""
        self.age = 0  # age and hunger score start at 0.
        self.hunger_score = 0
        return None

    def one_day(self):
        """Change in Bear's Age and Hunger Score After One Day."""
        self.age += 1  # increase age by 1.
        self.hunger_score -= 1  # decrease hunger score by 1.
        return None

    def eat(self, num_fish: int):
        """Adding the Number of fish a bear eats to hunger score."""
        self.hunger_score += num_fish
        return None
