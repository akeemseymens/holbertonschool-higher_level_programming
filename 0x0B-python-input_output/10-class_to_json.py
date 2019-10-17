#!/usr/bin/python3
"""
This is the "class to json" module.

"""


def class_to_json(obj):
    """Return the dict description for JSON serialization of an object."""
    return obj.__dict__
