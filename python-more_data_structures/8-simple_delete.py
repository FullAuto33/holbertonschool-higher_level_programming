#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary."""
    if key in a_dictionary:  # Si la clé existe dans le dictionnaire
        del a_dictionary[key]  # On supprime la clé du dictionnaire
    return a_dictionary  # Retourne le dictionnaire mis à jour
