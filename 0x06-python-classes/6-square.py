#!/usr/bin/python3
"""Calculate square"""


class Square:
    """Calculate Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and optional position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """return private size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """return private position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if (type(value) != tuple or len(value) != 2 or
            value[0] < 0 or value[1] < 0 or type(value[0]) is not int or
                type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """return current square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            if self.__position:
                for i in range(self.__position[1]):
                    print()
                for i in range(self.__size):
                    print(" " * self.__position[0], end="")
                    print("#" * self.__size)
            else:
                for i in range(self.__size):
                    print("#" * self.__size)
