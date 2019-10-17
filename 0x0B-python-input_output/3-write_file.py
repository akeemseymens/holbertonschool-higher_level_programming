#!/usr/bin/python3
"""
function to write a file.

"""


def write_file(filename="", text=""):
    """read a file."""

    with open(filename, 'w') as f:
        return f.write(str(text))
