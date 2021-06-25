"""
created by Nagaj at 25/06/2021
"""
from string import ascii_uppercase
import json
import os
from data import words
from validators import *
from logs import logger


DATA_PATH = "data.json"


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
        logger.info("data file found at '%s'", data_filepath)
        with open(data_filepath) as infile:
            return json.load(infile)
    logger.info("data file not found, return []")
    return []


def to_json(name: dict, names: list) -> None:
    """
    dump all nato names to json file
    :param name: single dictionary name nato
    :param names: list of nato names
    :return: None
    """
    if name not in names:
        names.append(name)
        with open(DATA_PATH, "w") as outfile:
            json.dump(names, outfile, indent=4)
        logger.info("payload [%s] was dumped successfully", name)
    else:
        logger.info("payload [%s] already added before", name)


def main():
    """
    entry point
    :return:
    """
    nato = dict(zip(ascii_uppercase, words))
    logger.info("All list nato alphabet mapping were loaded %s", nato)
    name = get_name()
    nato_for_name = {
        char: nato[char] for char in name
    }
    names = load_names()
    to_json(nato_for_name, names)


if __name__ == "__main__":
    main()
