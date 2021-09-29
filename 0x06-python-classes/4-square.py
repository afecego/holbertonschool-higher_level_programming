#!/usr/bin/python3
"""Square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.size = size

    @property
    def size(self):
        """return private var"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set var > 0 and integer"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """return square area"""
        return self.__size * self.__size
