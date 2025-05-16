#!/usr/bin/python3

def add_integer(a, b=98):
    """ Retourne la somme de deux entier"""
    if type(a) not in [int, float]:  # Si a n'est pas un entier
        raise TypeError("a must be an integer")
        # Retourne message d'erreur
    if type(b) not in [int, float]:  # Si b n'est pas un entier
        raise TypeError("b must be an integer")
        # Retourne message d'erreur
    return int(a) + int(b)  # Retourne la somme de a et b
