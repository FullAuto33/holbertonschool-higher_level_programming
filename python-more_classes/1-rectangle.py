#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Class Rectanngle defines rectangle"""
    def __init__(self, width=0, height=0):
        """Init with the width and height"""
        self.width = width
        self.height = height
        pass

    @property
    def width(self):
        """Retrieve for width"""
        return self.__width
        pass

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        pass

    @property
    def height(self):
        """Retrieve for height"""
        return self.__height
        pass

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        pass
