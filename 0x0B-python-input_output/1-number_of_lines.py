#!/usr/bin/python3
"""
This is number_of_lines function: using with statement to open file.

"""


def number_of_lines(filename=""):

    """function that returns number of lines."""
    count = 0
    with open(filename, 'r') as f:
        for i in f:
            count += 1

    return count
