#!/usr/bin/python3
"""class base"""
import json
import csv


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

        if list_objs is None:
            with open(file, "w") as fil:
                fil.write("[]")
        else:
            for obj in list_objs:
                line = obj.to_dictionary()
                new_list.append(line)

        with open(file, "w") as f:
            f.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if (cls.__name__ == "Square"):
            dummy = cls(3)
        if (cls.__name__ == "Rectangle"):
            dummy = cls(3, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        file = cls.__name__ + ".csv"

        with open(file, "w") as f:
            write = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for ob in list_objs:
                    write.writerow([ob.id, ob.width, ob.height, ob.x, ob.y])
            if cls.__name__ == "Square":
                for ob in list_objs:
                    write.writerow([ob.id, ob.size, ob.x, ob.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        file = cls.__name__ + ".csv"
        new_list = []

        with open(file, "r") as f:
            reader = csv.reader(f)
            for args in reader:
                if cls.__name__ == "Rectangle":
                    dictionary = {
                        "id": int(args[0]),
                        "width": int(args[1]),
                        "height": int(args[2]),
                        "x": int(args[3]),
                        "y": int(args[4])
                    }
                if cls.__name__ == "Square":
                    dictionary = {
                        "id": int(args[0]),
                        "size": int(args[1]),
                        "x": int(args[2]),
                        "y": int(args[3])
                    }
                new_list.append(cls.create(**dictionary))
        return new_list
