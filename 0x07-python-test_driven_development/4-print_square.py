#!/usr/bin/python3
"""
This is  "print_square

The print_square module prints integer representation with #
"""


def print_square(size):
    """
    Print a square with the character #

    """

    if not isinstance(size, int):
        raise ValueError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    print(('#' * size + '\n') * size, end='')
