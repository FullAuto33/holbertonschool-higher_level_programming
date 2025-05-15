#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element."""
    new_list = []  # Initialise une nouvelle liste vide
    for i in range(list_length):  # Pour chaque element de la liste
        try:  # Essaye de diviser les elements
            result = my_list_1[i] / my_list_2[i]
        except TypeError:  # Si l'un des elements n'est pas un nombre
            print("wrong type")  # Affiche mauvais type
            result = 0  # Resultat = 0
        except ZeroDivisionError:  # Si le diviseur est égal à 0
            print("division by 0")  # Affiche division par 0
            result = 0  # Resultat = 0
        except IndexError:  # Si l'index est hors de portée
            print("out of range")  # Affiche hors de portée
            result = 0  # Resultat = 0
        finally:  # toujours
            new_list.append(result)  # Ajoute le resultat à la nouvelle liste
    return new_list  # Retourne la nouvelle liste
