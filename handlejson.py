"""
created by Nagaj at 25/06/2021
"""
import os
import json
from logs import logger


DATA_PATH = "data.json"


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