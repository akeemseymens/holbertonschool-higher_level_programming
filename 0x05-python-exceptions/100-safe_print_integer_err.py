#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as type_value:
        sys.stderr.write("Exception: {}\n".format(type_value)

    return False
