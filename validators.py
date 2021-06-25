"""
created by Nagaj at 25/06/2021
"""

from logs import logger

MIN_NAME_LEN = 3
EMPTY = ""


def validate_no_number(function):
    """

    :param function: function return name as string input from user
    :return: validated name with no number
    """

    def check_has_numbers(name):
        logger.info("checking name if has number[s] '%s'", name)
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
            logger.error("invalid name with number[s] for '%s'", name)
            name = function(*args, **kwargs)
            has_number = check_has_numbers(name)
        logger.info("validated name with no number[s] for '%s'", name)
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
            logger.error("empty or short name for name '%s'", name)
            name = function()
        logger.info("validated length for name '%s'", name)
        return name

    return wrapper
