#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set."""
    return set_1 ^ set_2  # Retourne l'element qui est dans un seul des deux
