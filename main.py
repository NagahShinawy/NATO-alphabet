"""
created by Nagaj at 25/06/2021
"""
from string import ascii_uppercase
from data import words
from validators import *
from handlejson import *
from logs import logger


@validate_no_number
@validate_empty_and_len
def get_name() -> str:
    """
    name as string from user
    :return: name
    """
    return input("Please Enter Your Name. with no numbers")


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
