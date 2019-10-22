#!/usr/bin/python3
"""Class for square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        s = '[Square] ({:d}) {:d}/{:d} - {:d}'
        return s.format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the square"""
        if args:
            ls = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, ls[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dict representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
