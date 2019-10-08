#!/usr/bin/python3
""" A Rectangle Class """


class Rectangle:
    """ A Rectangle with a representation """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializing a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Print of a rectange"""
        ln = str(self.print_symbol) * self.width + '\n'
        return (self.height * ln).strip()

    def __repr__(self):
        """ Representation of instance constructor of the rectangle """
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        """ Print a message on deletion """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return the rectangle with bigger area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """ Create a square """
        return cls(size, size)

    @property
    def width(self):
        """ Get the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width to the value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
