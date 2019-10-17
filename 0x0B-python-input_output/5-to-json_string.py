#!/usr/bin/python3
"""
This is to_json to String.

"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object
    """
    import json
    return json.dumps(my_obj)
