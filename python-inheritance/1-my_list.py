#!/usr/bin/python3
""" Class MyList that inherits from list"""


class MyList(list):
    """ Class MyList that inherits from list """

    def print_sorted(self):  # Fonction qui affiche la liste triée
        """ Prints the list, but sorted (ascending sort) """
        print(sorted(self))  # Affiche la liste triée dans l'ordre croissant
