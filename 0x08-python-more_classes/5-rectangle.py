#!/usr/bin/python3
"""Rectangle definitions"""


class Rectangle:
    """Rectangle class representing"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return private width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the restangule"""
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """return private height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the restangule"""
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Return the area of rectangule"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of rectangule"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """prints in stdout the square with the character #"""
        st = ""
        if self.__width == 0 or self.__height == 0:
            pass
        else:
            st += "\n".join("#" * self.__width for j in range(self.__height))

        return st

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
