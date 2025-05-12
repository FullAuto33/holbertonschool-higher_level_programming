#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position."""
    if idx < 0 or idx >= len(my_list):
        # Si l'index est inferieur a 0 ou superieur a la longueur de la list
        return my_list  # Retourne la liste
    my_list[idx] = element  # Sinon remplace l'element a l'index par element
    return my_list  # Retourne la liste modifiee
