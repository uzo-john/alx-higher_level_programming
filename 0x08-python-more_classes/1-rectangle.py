#!/usr/bin/python3
"""
defines a Retangle class
"""

class Rectangle:
    """to represent a rectangle"""

    def __init__(self, width=0, height=0):

        """ method that Initializes the class rectangle
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """method that get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter that define the width of the rectangle
        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width  is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """methhod that get the height of the rectangle"""
        return self.__heigh

    @height.setter
    def height(self, value):
        """setter that define the height of the rectangle
        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """
        if isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
