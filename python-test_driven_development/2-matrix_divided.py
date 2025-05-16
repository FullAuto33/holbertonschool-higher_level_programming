#!/usr/bin/python3
"""Divides elements of matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if isinstance(matrix, list):
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError("\
                matrix must be a matrix (list of lists) of integers/floats")
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError("\
                    matrix must be a matrix (list of lists) \
                    of integers/floats")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
