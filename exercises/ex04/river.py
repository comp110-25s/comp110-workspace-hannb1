"""File to define River class."""

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear

__author__: str = "730557969"


class River:
    """Creating a new class called River!"""

    day: int  # attributes of River class.
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears!"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears.
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removing Fish and Bears from the River when get too old and die."""
        remaining_fish: list[Fish] = []  # fish still alive.
        remaining_bears: list[Bear] = []  # bears still alive.
        for fish in self.fish:  # going through age of each fish in list.
            if fish.age < 4:
                remaining_fish.append(fish)  # list of fish 3 and younger still alive.
        self.fish = remaining_fish  # replacing list of fish in River.
        for bear in self.bears:  # going through age of each bear in list.
            if bear.age < 6:
                remaining_bears.append(bear)  # list of bears 5 and younger still alive.
        self.bears = remaining_bears  # replacing list of bears in River.
        return None

    def remove_fish(self, amount: int):
        """Removes an amount of fish from the River, starting with front of the list."""
        counter: int = 0  # keeps track of how many fish in list gone through.
        while counter < amount:
            self.fish.pop(0)  # removes fish at index 0 from the list.
            counter += 1
        return None

    def bears_eating(self):
        """Simulating Bears eating fish from the River."""
        idx: int = 0
        while idx < len(self.bears):  # going through individual bears in list.
            if len(self.fish) > 5:  # if there is more than 5 fish in the River.
                self.bears[idx].eat(3)  # each bear in list will eat 3 fish.
                self.remove_fish(3)  # for each bear, 3 fish will be removed from River.
            idx += 1  # going to the next bear in the list.
        return None

    def check_hunger(self):
        """Checking if the bears are well-fed or don't have enough food."""
        bears_left: list[Bear] = []  # bears well-fed and still alive.
        for bear in self.bears:  # going through each bear in list.
            if bear.hunger_score >= 0:
                bears_left.append(
                    bear
                )  # if hunger score is 0 or above, they are alive.
        self.bears = bears_left  # updating the list of bears with ones still alive.
        return None

    def repopulate_fish(self):
        """Reproduction of Fish in the River."""
        n_fish: int = len(self.fish) // 2 * 4  # for every 2 fish, add 4 fish.
        idx: int = 0
        while idx < n_fish:  # adding amount of fish calculated above.
            fish: Fish = Fish()  # creating object of fish.
            self.fish.append(fish)  # adding object of fish to list.
            idx += 1
        return None

    def repopulate_bears(self):
        """Reproduction of Fish in the River."""
        n_bears: int = len(self.bears) // 2  # for every 2 bears, add 1 bear.
        idx: int = 0
        while idx < n_bears:  # adding amount of bears calculated above.
            bear: Bear = Bear()  # creating object of bear.
            self.bears.append(bear)  # adding object of bear to list.
            idx += 1
        return None

    def view_river(self):
        """Status of River by Day, reporting # of Fish and # of Bears!"""
        x: int = self.day  # current day.
        y: int = len(self.fish)  # population of fish.
        z: int = len(self.bears)  # population of bears.
        print(f"~~~ Day {x}: ~~~")  # printed output.
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Reports Status of River, day-by-day, for a week."""
        while self.day < 7:  # status of River for 7 days.
            self.one_river_day()  # uses information from one_river_day.
        return None
