#!/usr/bin/python3
"""Base Class"""

class Base:
    """Represents the Base clase"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def integer_validator(self, name, value):
        """Validate value."""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be >= 0'.format(name))

    def update(self, *args, **kwargs):
        """update the instance attributes"""
        if args:
            arr = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, arr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
