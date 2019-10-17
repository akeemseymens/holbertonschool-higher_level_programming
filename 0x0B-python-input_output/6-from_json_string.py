#!/usr/bin/python3
"""
This is from_json to String.

"""


def from_json_string(my_str):
    """
    Returns the JSON representation of an object
    """
    import json
    return json.loads(my_str)
