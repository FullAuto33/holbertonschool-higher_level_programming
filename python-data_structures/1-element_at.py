#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element from a list."""
    if idx < 0 or idx >= len(my_list):
        # Si l'index est inferieur a 0 ou superieur a la longueur de la liste
        return None  # Retourne None
    return my_list[idx]  # Sinon retourne l'element a l'index idx
