#!/usr/bin/python3
"""Description to module return pascal triangle"""


def pascal_triangle(n):
    """Return list of pascal triangle"""
    if n <= 0:
        # Si n est inferieur ou egal a 0
        return []
        # On retourne une liste vide

    triangle = [[1]]
    # On initialise le triangle avec la premiere ligne

    for i in range(1, n):
        # On parcourt les lignes du triangle
        prev_row = triangle[i - 1]  # On recupere la ligne precedente
        new_row = [1]  # On initialise la nouvelle ligne avec 1

        for j in range(1, len(prev_row)):
            # On parcourt les elements de la ligne precedente
            new_value = prev_row[j - 1] + prev_row[j]
            # On calcule la nouvelle valeur
            new_row.append(new_value)
            # On l'ajoute a la nouvelle ligne

        new_row.append(1)
        # On ajoute 1 a la fin de la nouvelle ligne
        triangle.append(new_row)
        # On ajoute la nouvelle ligne au triangle

    return triangle
    # On retourne le triangle
