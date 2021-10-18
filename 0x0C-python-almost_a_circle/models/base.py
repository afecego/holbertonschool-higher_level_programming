#!/usr/bin/python3
"""class base"""
import json


class Base():
    """Creation base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        new_list = []
        file = cls.__name__ + ".json"
        for row in list_objs:
            if row is None:
                return []
            for obj in list_objs:
                line = obj.to_dictionary()
                new_list.append(line)

        with open(file, "w") as f:
            f.write(Base.to_json_string(new_list))
