#!/usr/bin/python3
def magic_string():
    magic_string.a = getattr(magic_string, 'a', 0) + 1
    return ', '.join(['Holberton'] * magic_string.a)
