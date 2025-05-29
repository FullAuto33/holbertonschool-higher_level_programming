#!/usr/bin/python3
"""Square #1"""


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
        return self.__width * self.__height

    def __str__(self):
        """Return str of rectangle."""
        return "[Rectangle] {}/{}" .format(self.__width, self.__height)


class Square(Rectangle):
    """Square ineherit from Rectangle."""
    def __init__(self, size):
        """Init square with size"""
        super().__init__(size, size)  # On appelle init de la classe parent
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
