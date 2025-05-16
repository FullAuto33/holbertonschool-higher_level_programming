#!/usr/bin/python3
"""Divides elements of matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number"""
    if not isinstance(matrix, list):
        # verifie si c'est une liste de listes
        raise TypeError("matrix must be a matrix\
        (list of lists) of integers/floats")
        # Retourne typeError si ce n'est pas une liste de listes
    if not all(isinstance(row, list) for row in matrix):
        # verifie si chaque element de la matrice est une liste
        raise TypeError("matrix must be a \
        matrix (list of lists) of integers/floats")
        # Retourne typeError si ce n'est pas une liste de listes
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        # verifie si c'est une liste de listes d'entiers ou de flottants
        raise TypeError("matrix \
        must be a matrix (list of lists) of integers/floats")
        # Retourne typeError si c'est pas entier ou flottant
    if div == 0:  # Si div est égal à 0
        raise ZeroDivisionError("division by zero")
        # Retourne ZeroDivisionError si div est égal à 0
    if not isinstance(div, (int, float)):
        # verifie si div est un entier ou un flottant
        raise TypeError("div must be a number")
        # Retourne typeError si div n'est pas un entier ou un flottant
    if len(matrix) == 0 or len(matrix[0]) == 0:
        # Si la matrice est vide ou si la première ligne est vide
        return []  # Retourne une matrice vide
    if not all(len(row) == len(matrix[0]) for row in matrix):
        # verifie si toutes les lignes
        # de la matrice sont de la même taille
        raise TypeError("Each row of the matrix must have the same size")
        # Retourne typeError si toutes les lignes
        # de la matrice ne sont pas de la même taille

    return [[round(num / div, 2) for num in row] for row in matrix]
    # Retourne la matrice divisée par div pour chaque element de la matrice
