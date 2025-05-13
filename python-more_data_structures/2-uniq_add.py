#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    unique_list = set(my_list)
    # on recupere uniquement les integers
    total_sum = sum(unique_list)
    # on fait la somme des integers de la liste
    return total_sum  # on retourne la somme
