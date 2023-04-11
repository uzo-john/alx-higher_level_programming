#!/usr/bin/python3
class BaseGeometry:
    """ Class that defines the attributes of Geometric Shapes """

    def area(self):
        """method that defines the area of the geometric"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that recieves the value property
        Árgs:
            name: name of the object
            value: value of the property
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
