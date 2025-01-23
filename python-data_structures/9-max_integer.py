#!/usr/bin/python3
def max_integer(my_list=[]):
    taille = len(my_list)
    if not taille:
        return None
    else:
        compteur = my_list[0]
        for i in my_list[1:]:
            if i > compteur:
                compteur = i
        return compteur
