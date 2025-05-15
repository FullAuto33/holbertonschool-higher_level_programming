#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides two integers and prints the result."""
    try:  # Essaye de diviser a par b
        result = a / b  # Resultat = a / b
    except ZeroDivisionError:  # Si b est égal à 0
        result = None  # Resultat = None
    finally:  # On affiche toujours
        print("Inside result: {}".format(result))  # Affiche le resultat
    return result  # Retourne le resultat
