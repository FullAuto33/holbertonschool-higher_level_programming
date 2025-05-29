#!/usr/bin/python3
"""Full rectangle"""


class BaseGeometry:
    """BaseGeometry class with area method."""
    def area(self):
        """Raise exception if area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if value is an int greater 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inherit from BaseGeometry."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        print("[Rectangle] {}/{}" .format(self.__width, self.__height))
        return self.__width * self.__height
