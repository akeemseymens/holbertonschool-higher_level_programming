#!/usr/bin/python3
"""
This is MyList class.
print_sorted definition that sorted ascending order.

"""


class MyList(list):
    """Represents a MyList."""

    def print_sorted(self):
        """Print the list in sorted ascending order."""
        print(sorted(self))
