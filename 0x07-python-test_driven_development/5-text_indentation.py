#!/usr/bin/python3
"""
This is the "text indentation" module

The text indentation module take in text string.
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after these characters: . ? :
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for c, l in text:
        for l in '.?:':
            print('\n')
