#!/usr/bin/python3
"""Module defining a Square class"""


class Square:
    """Class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square"""
        self.size = size  # Utilise le setter pour la validation
        self.position = position  # Utilise le setter pour la validation

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Validates and sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Validates and sets the position of the square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square with '#' characters"""
        if self.__size == 0:
            print("")
            return

        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
