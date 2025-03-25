"""Function Skeletons for Exercise 3!"""

__author__ = "730557969"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    result: dict[str, str] = {}  # empty result dictionary
    for key in dictionary:  # iterating through keys in input dictionary
        old_value: str = dictionary[key]  # old_value is the values in input dictionary
        if old_value in result:  # cannot have duplicate keys
            raise KeyError("This key is already in result dictionary")
        else:
            result[old_value] = key  # inverting dictionary's keys and values in result
    return result  # inverted dictionary


def count(list1: list[str]) -> dict[str, int]:
    result_dict: dict[str, int] = {}  # empty result dictionary
    idx: int = 0  # to go through indexes of list
    while idx < len(list1):  # so do not go past length of list and get error
        if list1[idx] in result_dict:  # add to count at that key if already exists
            result_dict[list1[idx]] += 1
        else:  # start a new count located at a new key
            result_dict[list1[idx]] = 1
        idx += 1  # go to next item in list
    return result_dict  # item in list and associated times it shows up in list


def favorite_color(name_and_fav: dict[str, str]) -> str:
    new_dictionary: dict[str, int] = {}
    for key in name_and_fav:  # iterating through keys in name_and_fav
        color = name_and_fav[key]  # color is value at specified key
        if color in new_dictionary:  # adding onto existing key in new_dictionary
            new_dictionary[color] += 1
        else:  # creating new key in new_dictionary
            new_dictionary[color] = 1
    max: int = 0  # count of most votes for color
    max_color: str = ""  # color with most votes
    for key in new_dictionary:  # iterating through new_dictionary
        count = new_dictionary[key]  # count is the values of new_dictionary (number)
        if count > max:  # replace with new color if come across one with more votes
            max = count
            max_color = key
    return max_color  # color with the most votes


def bin_len(list_of_str: list[str]) -> dict[int, set[str]]:
    end_dict: dict[int, set[str]] = {}  # empty dictionary
    for word in list_of_str:  # words found in the list
        if len(word) in end_dict:  # already existing key in new_dict--just adding
            end_dict[len(word)].add(word)
        else:  # creating new key in end_dict
            end_dict[len(word)] = {word}
    return end_dict  # length of items and set of items applicable
