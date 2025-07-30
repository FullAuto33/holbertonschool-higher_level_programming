#!/usr/bin/python3
"""Description for the module."""


class Student:
    """Description for the Student class."""

    def __init__(self, first_name, last_name, age):
        """Descriptiojn for the initialization method."""
        self.first_name = first_name #Attribue la valeur prénom à l’objet
        self.last_name = last_name #Attribue la valeur nom à l’objet
        self.age = age #Attribue la valeur âge à l’objet

    def to_json(self):
        """Returns the dictionary representation of the Student."""
        return self.__dict__ # Retourne le dictionnaire de tout les objets