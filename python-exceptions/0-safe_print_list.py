#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ prints x elements of a list"""
    compteur = 0  # Initialise 0 a compteur
    for i in range(x):  # On parcours la liste
        try:  # On essaye d'afficher l'element i
            print(my_list[i], end="")
            # on affiche l'element i sans retour a la ligne
            compteur += 1  # On incremente le compteur
        except IndexError:  # Si l'index n'existe pas
            break  # On sort de la boucle
    print()  # On affiche un retour a la ligne
    return compteur  # On retourne le compteur
