#!/usr/bin/python3
"""Description module Square"""


class Square:
    """Class of Square"""
    def __init__(self, size=0):
        """ definie a square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        result = self.__size * self.__size
        return (result)
