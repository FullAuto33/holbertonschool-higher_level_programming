#!/usr/bin/python3
"""Improve Geometry"""


class BaseGeometry:
    """BaseGeometry class with area method."""
    def area(self):
        """Raise exception if area is not implemented."""
        raise Exception("area() is not implemented")
