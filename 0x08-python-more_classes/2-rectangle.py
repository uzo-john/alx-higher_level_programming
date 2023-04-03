#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
    """Initializes the rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that returns the value of the width
        Returns:
            rectangle width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height
        Returns:
            rectangle height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
