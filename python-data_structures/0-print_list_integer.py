#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints all integers of a list."""
    for i in my_list:  # Pour chaque element de my_list
        print("{:d}".format(i))  # Affiche l'element i
