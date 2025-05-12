#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:  # Si la liste est vide
        return None  # Renvoie None
    max_int = my_list[0]
    # Initialise max_int avec le premier élément de la liste
    for i in my_list:  # Parcourt chaque élément de la liste
        if i > max_int:  # Si l'élément i est supérieur à max_int
            max_int = i  # max_int devient i
    return max_int  # Renvoie max_int qui est le plus grand entier de la liste
