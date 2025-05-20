#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0):
        """Init size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        pass

    def area(self):
        """Returns current square area"""
        return self.size * self.size
        pass

    @property
    def size(self):
        """Retrieve for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        pass
