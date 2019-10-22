#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        s = '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'
        return s.format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    def area(self):
        """Area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Print the Rectangle to stdout"""
        for _ in range(self.y):
            print('')
        print(((' ' * self.x + '#' * self.width + '\n') * self.height).rstrip())

    def update(self, *args, **kwargs):
        """update the instance attributes"""
        if args:
            arr = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, arr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dict repr of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
