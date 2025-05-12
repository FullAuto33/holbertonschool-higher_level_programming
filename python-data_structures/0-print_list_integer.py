#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints all integers of a list."""
    for i in my_list: #pour chaque element de my_list
        print("{:d}".format(i)) #affiche l'element i
