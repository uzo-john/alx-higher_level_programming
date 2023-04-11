#!/usr/bin/python3
"""
Function that return the list of a lookup function
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
