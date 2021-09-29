#!/usr/bin/python3
"""Square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Constructor class size of square"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """return square"""
        return self.__size * self.__size
