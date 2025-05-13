#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """Returns a list with all values multiplied by a number."""
    result = []  # On initialise une liste vide
    for i in range(len(my_list)):  # On parcourt la liste
        result.append(my_list[i] * number)
        # On ajoute le resultat de la multiplication à la liste
    return result  # On retourne la liste
