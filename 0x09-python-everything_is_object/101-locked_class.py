#!/usr/bin/python3


class LockedClass(object):
    __slots__ = ['first_name']

    def __init__(self, v=0):
        self.first_name = v