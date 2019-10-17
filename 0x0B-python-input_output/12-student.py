#!/usr/bin/python3
class Student:
    """Represents a Student."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve specified attributes of a Student."""
        st_attr = {}
        if attrs is None:
            return self.__dict__
        for key in attrs:
            if key in self.__dict__.keys():
                st_attr[key] = self.__dict__[key]
        return st_attr
