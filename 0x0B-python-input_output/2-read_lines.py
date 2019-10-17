#!/usr/bin/python3
"""
This is read_lines function: reads n lines of a text file (UTF8)
and prints it to stdout:

"""


def read_lines(filename="", nb_lines=0):

    """function that returns number of lines."""
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
            return
        count = 0
        for l in f:
            if count < nb_lines:
                print(l, end='')
            count += 1
