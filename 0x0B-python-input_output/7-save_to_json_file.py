#!/usr/bin/python3
"""
This is from_json to String.

"""


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
