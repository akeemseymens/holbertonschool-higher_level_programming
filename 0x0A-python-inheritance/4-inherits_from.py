#!/usr/bin/python3
"""
This is inherits_from checks if an object is an instance in a class.

"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from
    the specified class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
