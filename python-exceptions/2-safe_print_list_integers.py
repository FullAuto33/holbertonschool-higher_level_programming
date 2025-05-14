#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ prints the first x elements of a list and only integers """
    compteur = 0  # Initialise 0 a compteur
    for i in range(x):  # On parcours la liste
        try:  # On essaye d'afficher l'element i
            print("{:d}".format(my_list[i]), end="")  # Affiche l'element i
            compteur += 1  # On incremente le compteur
        except (ValueError, TypeError):  # Si l'element n'est pas un entier
            continue  # On passe a l'element suivant
    print()  # On affiche un retour a la ligne
    return compteur  # On retourne le compteur
