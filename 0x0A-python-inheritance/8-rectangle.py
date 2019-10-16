#!/usr/bin/python3
"""
BaseGeometry class
area that is not yet implemented.
integer validator that validates value and that it is not negative.
Rectangle class represents the rectangle.

"""


class BaseGeometry:
    """Represents a BaseGeometry."""

    def area(self):
        """Raise an exception."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate value."""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Represents a rectangle."""
    def __init__(self, width, height):
        """Initialize rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
