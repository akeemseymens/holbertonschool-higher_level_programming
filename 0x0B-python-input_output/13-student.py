#!/usr/bin/python3
"""
This is the Student module.

"""


class Student:
    """Represents a Student."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve specified attributes of a Student."""
        if not attrs:
            return self.__dict__
        st_attrs = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                st_attrs[key] = value
        return my_attrs

    def reload_from_json(self, json):
        """Replace attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
