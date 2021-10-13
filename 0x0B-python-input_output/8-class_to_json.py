#!/usr/bin/python3
"""function that returns the dictionary description
with simple data structure"""
import json


def class_to_json(obj):
    """JSON serialization of an object"""
    try:
        return obj.toJSON()
    except Exception as ex:
        return obj.__dict__
