#!/usr/bin/python3
def element_at(my_list, idx):
    taille = len(my_list)
    if idx < 0 or idx >= taille:
        return None
    else:
        return my_list[idx]
