#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):

    if isinstance(obj, a_class):
        return True
    return False
