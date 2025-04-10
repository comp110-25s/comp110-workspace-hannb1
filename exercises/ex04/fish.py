"""File to define Fish class."""

__author__: str = "730557969"


class Fish:
    """Creating a new class called Fish!"""

    age: int  # attribute of Fish.

    def __init__(self):
        """Initializing a Fish class object."""
        self.age = 0  # age starts at 0.
        return None

    def one_day(self):
        """Change in a fish's age after one day."""
        self.age += 1
        return None
