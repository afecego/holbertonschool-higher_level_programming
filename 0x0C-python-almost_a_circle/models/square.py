#!/usr/bin/python3
"""class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Construct"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square] ({:}) {:}/{:} - {:}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """property size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is int:
            if value > 0:
                self.width = value
                self.height = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the to_dictionary of square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
