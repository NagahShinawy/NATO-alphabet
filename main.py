"""
created by Nagaj at 25/06/2021
"""
from string import ascii_uppercase
import json
import os
from data import words

DATA_PATH = "data.json"
MIN_NAME_LEN = 3
EMPTY = ""


def validate_no_number(function):
    """

    :param function: function return name as string input from user
    :return: validated name with no number
    """
    def check_has_numbers(name):
        has_number = False
        for char in name:
            if char.isdigit():
                has_number = True
                break
        return has_number

    def wrapper(*args, **kwargs):
        name = function(*args, **kwargs)
        has_number = check_has_numbers(name)
        while has_number:
            name = function(*args, **kwargs)
            has_number = check_has_numbers(name)
        return name

    return wrapper


def validate_empty_and_len(function):
    """
    validate if name is empty or short length
    :param function: function that return name of user
    :return: validated name [not empty, more that 3 char]
    """

    def wrapper(*args, **kwargs):
        name = function(*args, **kwargs)

        while name == EMPTY or len(name) < MIN_NAME_LEN:
            name = function()
        return name

    return wrapper


@validate_no_number
@validate_empty_and_len
def get_name() -> str:
    """
    name as string from user
    :return: name
    """
    return input("Please Enter Your Name. with no numbers")


def load_names() -> list:
    """
    load all nato names from json file if it exist else empty list
    :return: list of names of data json file if it exist else empty list
    """
    data_filepath = os.path.join(os.getcwd(), "data.json")
    is_exist = os.path.isfile(data_filepath)
    if is_exist:
        with open(data_filepath) as infile:
            return json.load(infile)
    return []


def to_json(name: dict, names: list) -> None:
    """
    dump all nato names to json file
    :param name: single dictionary name nato
    :param names: list of nato names
    :return: None
    """
    names.append(name)
    with open(DATA_PATH, "w") as outfile:
        json.dump(names, outfile, indent=4)


def main():
    """
    entry point
    :return:
    """
    nato = dict(zip(ascii_uppercase, words))
    name = get_name()
    nato_for_name = {
        char.upper(): nato.get(char.upper()) for char in name if char.upper() in nato
    }
    names = load_names()
    to_json(nato_for_name, names)


if __name__ == "__main__":
    main()
