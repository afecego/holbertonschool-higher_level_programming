#!/usr/bin/python3
"""Write a class Student"""


class Student():
    """defines a student"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if type(attrs) is list:
            if (type(line) is str for line in attrs):
                eq = {k: getattr(self, k) for k in attrs if hasattr(self, k)}
                return eq
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student"""
        if json is not None:
            for attr, value in json.items():
                setattr(self, attr, value)
