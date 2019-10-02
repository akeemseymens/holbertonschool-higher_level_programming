#!/usr/bin/python3
class Square:
    """ Represents a square"""
    def __init__(self, size=0):
        """intialize data: size """
        self.__size = size

    @property
    def size(self):
        """Getting size """
        return self.__size

    @size.setter
    def size(self, value):
        """Setting size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size**2
    def my_print(self):
        """Returns the current square"""
        if self.__size == 0:
            print()
        else:
            for l in range(self.__size):
                print('#' * self.__size)
