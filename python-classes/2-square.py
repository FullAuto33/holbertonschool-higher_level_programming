#!/usr/bin/python3
"""Class square defines square by size"""


class Square:
    """Class Square that defines a square"""
    def __init__(self, size=0):
        """Init size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        pass
