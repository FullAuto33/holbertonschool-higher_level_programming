#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order."""
    if my_list is not None:  # Si my_list n'est pas vide
        for i in reversed(my_list):  # Pour chaque element de my_list inversé
            print("{:d}".format(i))  # Affiche l'element i
