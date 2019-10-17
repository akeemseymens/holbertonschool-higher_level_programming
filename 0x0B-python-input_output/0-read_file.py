#!/usr/bin/pyhon3
"""
function to read a file.

"""


def read_file(filename=""):
    """read a file."""

    with open(filename, 'r') as f:
        print(f.read(), end='')
