#!/usr/bin/python3
def carre(x):
    return (x**2)
def square_matrix_simple(matrix=[]):
    result = matrix[:]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i] = list(map(carre, matrix[i]))
    return result
