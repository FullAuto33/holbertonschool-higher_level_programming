#!/usr/bin/python3
"""prints a square with the character #"""


def print_square(size):
    """prints a square with the character #"""
    if not isinstance(size, int):  # Verifie si size est un entier
        raise TypeError("size must be an integer")  # Retourne TypeError
    if size < 0:  # Verifie si size est négatif
        raise ValueError("size must be >= 0")  # Retourne ValueError
    for i in range(size):  # Pour chaque ligne de la matrice
        print("#" * size)  # Affiche le carré de #
