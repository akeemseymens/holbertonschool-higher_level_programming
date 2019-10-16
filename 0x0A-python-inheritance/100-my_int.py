#!/usr/bin/python3
class MyInt(int):
    """Represents a MyInt."""
    pass

    def __eq__(self, other):
        """Check if two MyInts are equal."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Check if two MyInts are not equal."""
        return int(self) == int(other)
