"""Running Unit Tests to Determine Whether Functions in dictionary.py Run Correctly"""

__author__ = "730557969"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len
import pytest

# have to import files to be able to use functions in this new file


def test_invert_use1() -> None:
    """First Use Case Unit Test for Invert Function"""
    """Testing if Invert dictionary containing two items"""
    """The values in input dictionary cannot be the same--will become keys"""
    assert invert({"1": "dog", "2": "cat"}) == {"dog": "1", "cat": "2"}


def test_invert_use2() -> None:
    """Second Use Case Unit Test for Invert Function"""
    """Testing if invert dictionary containing three value"""
    assert invert({"pet": "dog", "tank": "fish", "stable": "horse"}) == {
        "dog": "pet",
        "fish": "tank",
        "horse": "stable",
    }


def test_invert_edge() -> None:
    """Edge Case Unit Test for Invert Function"""
    """Testing if Correctly return empty dictionary"""
    assert invert({}) == {}


with pytest.raises(KeyError):
    my_dictionary = {"dog": "1", "cat": "1"}
    invert(my_dictionary)

# testing if KeyError is correctly raised for invert function


def test_count_use1() -> None:
    """First Use Case Unit Test for Count Function"""
    """Testing if list with a repeat of c works correctly """
    assert count(["a", "b", "c", "c"]) == {"a": 1, "b": 1, "c": 2}


def test_count_use2() -> None:
    """Second Use Case Unit Test for Count Function"""
    """Testing if list with no repeats works correctly"""
    assert count(["a", "b"]) == {"a": 1, "b": 1}


def test_count_edge() -> None:
    """Edge Case Unit Test for Count Function"""
    """Testing if empty list returns empty dictionary"""
    assert count([]) == {}


def test_favorite_color_use1() -> None:
    """First Use Case Unit Test for Favorite Color Function"""
    """Testing if it correctly returns the most seen favorite color (no tie)"""
    assert (
        favorite_color({"1": "yellow", "2": "blue", "3": "blue", "4": "orange"})
        == "blue"
    )


def test_favorite_color_use2() -> None:
    """Second Use Case Unit Test for Favorite Color Function"""
    """Testing if it corrrecly returns Tie for Favorite Color"""
    assert (
        favorite_color(
            {"1": "blue", "2": "blue", "3": "yellow", "4": "yellow", "5": "orange"}
        )
        == "blue"
    )


def test_favorite_color_edge() -> None:
    """Edge Case Unit Test for the Favorite Color Function"""
    """Testing if Correctly return empty string for empty dictionary input"""
    assert favorite_color({}) == ""


def test_bin_len_use1() -> None:
    """First Use Case Unit Test for the Bin Length Function"""
    """Testing if Correctly Creates Dictionary with one str for each number category"""
    assert bin_len(["my", "dog", "Teddy"]) == {2: {"my"}, 3: {"dog"}, 5: {"Teddy"}}


def test_bin_len_use2() -> None:
    """Second Use Case Unit Test for the Bin Length Function"""
    """Testing if Correctly returns > than one str in set for result"""
    assert bin_len(["cat", "dog", "pig", "horse"]) == {
        3: {"cat", "dog", "pig"},
        5: {"horse"},
    }


def test_bin_length_edge() -> None:
    """Edge Case Unit Test for the Bin Length Function"""
    """Testing if an Empty List returns correctly an empty dictionary"""
    assert bin_len([]) == {}
