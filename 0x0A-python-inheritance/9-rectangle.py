#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle. """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """To return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """method that returns the printable string """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
