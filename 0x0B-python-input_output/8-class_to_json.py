#!/usr/bin/python3
"""
Contains the "class_to_json" function
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return obj.__dict__

