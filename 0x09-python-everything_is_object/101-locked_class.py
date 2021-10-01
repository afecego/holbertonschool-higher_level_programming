#!/usr/bin/python3
"""Locked class"""


class LockedClass(object):
    """Locking class"""
    __slots__ = ['first_name']

    def __init__(self, v=0):
        """initialization of class"""
        self.first_name = v
