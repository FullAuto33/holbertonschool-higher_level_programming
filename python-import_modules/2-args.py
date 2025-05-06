#!/usr/bin/python3
if __name__ == "__main__":
    """ Print the number of arguments and their values"""
    import sys  # Import la bibliothèque sys
    count = len(sys.argv) - 1  # compte le nombre d'arguments
    if count == 0:  # Si le nombre d'arguments est égal à 0
        print("0 arguments.")  # Affiche 0 arguments
    elif count == 1:  # Si le nombre d'arguments est égal à 1
        print("1 argument:")  # Affiche 1 argument
    else:  # Si le nombre d'arguments est supérieur à 1
        print("{} arguments:".format(count))  # Affiche le nombre d'arguments
    for i in range(count):  # Pour chaque argument
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
        # Affiche la position et la valeur de l'argument
