#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Init size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position
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

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
        pass

    @property
    def position(self):
        """Retrieve for position"""
        return self.__position
        pass

    @position.setter
    def position(self, value):
        """Setter for position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        pass
