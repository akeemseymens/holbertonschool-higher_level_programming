#!/usr/bin/python3
"""
class that represents rectangle that inherits basegeometry object attributes.
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
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __repr__(self):
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height
