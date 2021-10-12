#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """class inherits from list"""
    def print_sorted(self):
        """Methodo print list sorted"""
        print(sorted(self))
