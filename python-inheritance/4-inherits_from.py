#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """Function return true if is an instance inherited of a class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
    # Retourne Vrai si l'objet est une instance d'une classe
    # héritée de la classe spécifiée
