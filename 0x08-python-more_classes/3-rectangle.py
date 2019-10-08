#!/usr/bin/python3


class Rectangle:
    """Represents a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize the data."""
        self.__width = width
        self.__height = height

    def __str__(self):
        """Print the rectangle."""
        return (self.height * ('#' * self.width + '\n')).strip()

    @property
    def width(self):
        """Getting the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
