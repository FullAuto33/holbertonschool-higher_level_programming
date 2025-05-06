#!/usr/bin/python3
if __name__ == "__main__":
    """ Print result of the addition of all arguments"""
    from sys import argv  # Import la bibliothèque sys
    result = 0  # Initialise le résultat à 0
    for i in range(1, len(argv)):  # Pour chaque argument
        result += int(argv[i])  # Ajoute l'argument à la somme
    print("{}".format(result))  # Affiche le résultat
