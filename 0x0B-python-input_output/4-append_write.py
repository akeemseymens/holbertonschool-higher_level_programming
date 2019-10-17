#!/usr/bin/pyhon3
"""
function to appends to a file.

"""


def append_write(filename="", text=""):
    """append to a file."""

    with open(filename, 'a') as f:
        return f.write(str(text))
