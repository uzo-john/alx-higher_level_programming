#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false

    Args:
	obj: object
	a_class: class type
    """

    return type(obj) is a_class
