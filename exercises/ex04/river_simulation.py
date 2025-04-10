"""My River Simulation!"""

from exercises.EX04.river import River

__author__: str = "730557969"


my_river: River = River(10, 2)  # new River object with 10 fish and 2 bears.

my_river.view_river()  # calling the view_river method.

my_river.one_river_week()  # calling the one_river_week method.
