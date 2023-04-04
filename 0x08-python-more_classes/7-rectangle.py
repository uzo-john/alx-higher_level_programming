#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """represent a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """return the printable string represtation
        of the rectangle
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height):
            rectangle += ("#" * self.__width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """method to print a message for every delection of a rectangle"""

        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")
