#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from a string."""
    newstr = ""  # Create nouvelle str
    for letter in my_string:  # Pour chaque lettre dans la str
        if letter != 'c' and letter != 'C':  # Si la lettre n'est pas c ou C
            newstr += letter  # Ajoute la lettre a la nouvelle str
    return newstr  # Retourne la nouvelle str
