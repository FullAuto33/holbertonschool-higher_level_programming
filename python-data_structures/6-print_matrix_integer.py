#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        compteur = 0
        for y in matrix[x]:
            print("{:d}".format(y), end="")
            if compteur < len(matrix[x]) - 1:
                print(end=" ")
            compteur += 1
        print()
