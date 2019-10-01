#!/usr/bin/python3
class Square:
    """ Represents a square"""
    def __init__(self, size=0):
        """intialize data: size """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
