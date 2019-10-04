#!/usr/bin/python3
"""
This is  "add_integer" module

The add_integer module adds two variables together.
"""
def add_integer(a, b=98):
    """
    Returns the sum of a and b, cast them as integers.

    """
    if isinstance(a, (int,float)) is False:
        raise TypeError('a must be an integer')
    if isinstance(b, (int,float)) is False:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
