#!/usr/bin/python3
"""Shapes, Interfaces, and Duck Typing"""


from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract Shape Class"""

    @abstractmethod
    def area(self):
        """Abstract area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract perimeter"""
        pass


class Circle(Shape):
    """Circle class inherit Shape"""

    def __init__(self, radius):
        """Init circle with radius"""
        self.radius = radius

    def area(self):
        """Return area of circle"""
        pi = 3.14159
        return pi * self.radius ** 2

    def perimeter(self):
        """Return perimeter of circle"""
        pi = 3.14159
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class inherit Shape"""

    def __init__(self, width, height):
        """Init rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter"""

    print("Area: {}" .format(shape.area()))
    print("Perimeter: {}" .format(shape.perimeter()))
