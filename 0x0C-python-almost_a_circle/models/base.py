#!/usr/bin/python3
"""Base Class"""
import json
import csv
import os.path


class Base:
    """Represents the Base clase"""
    __nb_objects = 0

    def __init__(self, id=None):
        """intialialized the base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def update(self, *args, **kwargs):
        """update the instance attributes"""
        if args:
            arr = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, arr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @staticmethod
    def to_json_string(list_dictionaries):
        """sharing data representation"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Convert a json string to a Python object"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string of list_obj to a file"""
        if list_objs is None:
            list_objs = []
        with open(cls.__name__ + '.json', 'w') as f:
            things = [x.to_dictionary() for x in list_objs]
            f.write(Base.to_json_string(things))

    @classmethod
    def create(cls, **dictionary):
        """Create a new Base instance with kwargs"""
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = str(cls).split(".")[-1][:-2] + ".json"
        if not os.path.exists(filename):
            return []
        res = []
        with open(filename, "r") as f:
            dicts = cls.from_json_string(f.readline())
        for d in dicts:
            res.append(cls.create(**d))
        return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save a list of objects represented as csv in a file"""
        with open(cls.__name__ + '.csv', 'w') as f:
            text = ''
            for o in list_objs:
                if cls.__name__ == 'Square':
                    fs = '{:d},{:d},{:d},{:d}\n'
                    text += fs.format(o.id, o.size, o.x, o.y)
                else:
                    fs = '{:d},{:d},{:d},{:d},{:d}\n'
                    text += fs.format(o.id, o.width, o.height, o.x, o.y)
            f.write(text)
