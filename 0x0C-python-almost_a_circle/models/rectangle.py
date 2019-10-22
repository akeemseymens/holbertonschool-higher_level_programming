#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """print out message"""
        s = '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'
        return s.format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """Setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Getter for width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Getter for height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Setter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Getter for x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Print in std the rectangle with the character '#'."""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """update the instance attributes"""
        if args:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dict represetation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
