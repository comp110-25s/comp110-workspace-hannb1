"""This program will help calculate what is needed for the perfect tea party!"""

__author__: str = "730557969"


def main_planner(guests: int) -> None:
    """Main Function of the Tea Party Planner"""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(
                tea_count=(tea_bags(people=guests)), treat_count=(treats(people=guests))
            )
        )
    )


def tea_bags(people: int) -> int:
    """Calculation of number of tea bags needed for the party"""
    return 2 * people


def treats(people: int) -> int:
    """Calculation of number of treats needed for the party"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculation of total cost"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
