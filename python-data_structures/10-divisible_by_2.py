#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    multiple = []  # Creation liste vide
    for i in my_list:  # Parcourt chaque élément de la liste
        if i % 2 == 0:  # Si l'élément i est divisible par 2
            multiple.append(True)  # Ajoute True à la liste
        else:  # Sinon
            multiple.append(False)  # Ajoute False à la liste
    return multiple  # Renvoie la liste des multiples de 2
