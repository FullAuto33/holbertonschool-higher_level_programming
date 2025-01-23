#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix=[[]]:
        print()
    else:
        for i in matrix:
            for y in i:
                print('{:d}'.format(y), end=' ' if y != i[-1] else '\n')
