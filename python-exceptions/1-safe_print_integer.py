#!/usr/bin/python3

def safe_print_integer(value):
    """ prints an integer with "{:d}".format() """
    try:  # Essaye de convertir la valeur en entier
        print("{:d}".format(value))  # Affiche la valeur
        return True  # Retourne True si la valeur est un entier
    except (TypeError, ValueError):  # Si la valeur n'est pas un entier
        return False  # Retourne False si la valeur n'est pas un entier
