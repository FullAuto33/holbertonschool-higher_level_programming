#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    if matrix == [[]]:
        print()
    else:
        for ligne in matrix:  # Pour chaque ligne dans la matrice
            for colone in ligne:  # Pour chaque colonne dans la ligne
                if colone != ligne[-1]:
                    # Si ce n'est pas le dernier élément de la ligne
                    print("{:d}".format(colone), end=" ")
                    # Affiche l'élément avec un espace
                else:  # Si c'est le dernier élément de la ligne
                    print("{:d}".format(colone), end="\n")
                    # Affiche l'élément avec un retour à la ligne
