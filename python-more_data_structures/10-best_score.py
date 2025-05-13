#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not a_dictionary:  # Si le dictionnaire est vide
        return None  # On retourne None
    return max(a_dictionary, key=a_dictionary.get)
    # On retourne la clé avec la valeur maximale
