#!/usr/bin/python3
"""

based on a class that defines a Rectangle


"""


class Rectangle:
    """class that define a rectangle"""

    def __init__(self, height = 0, width = 0):

        """ method that Initializes the class rectangle"""

        self.height = height
        self.width = width

    @property
    def width(self):
        """method that return the value of the width of the rectangle"""

        return:
		self.__width

    @width.setter
    def width(self, value):

        """setter that set the width of the rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method that return the value of the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter that set the hright of the rectangle"""
        if type(value) is not int:
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
