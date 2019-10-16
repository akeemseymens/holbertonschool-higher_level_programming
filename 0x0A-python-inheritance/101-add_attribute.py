#!/usr/bin/python3
"""
This is a function to add attributes to an object.

"""


def add_attribute(obj, name, value):
    """Add an attribute to an object"""
    if getattr(obj, '__dict__', None) is None:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
