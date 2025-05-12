#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete the item at a specific index in a list."""
    if idx < 0 or idx >= len(my_list):
        # Si l'index est négatif ou supérieur à la longueur de la liste
        return my_list  # Renvoie la liste sans modification
    del my_list[idx]  # Supprime l'élément à l'index idx
    return my_list  # Renvoie la liste modifiée
