#!/usr/bin/python3
class Square:
    """ Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """intialize data: size """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """Getting position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size**2

    def my_print(self):
        """Prints the square from the size and position"""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end="")
            for i in range(self.__size):
                    print(" " * self.__position[0], end="")
                    print("#" * self.__size)
