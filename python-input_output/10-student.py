#!/usr/bin/python3
"""Description for the module."""


class Student:
    """Description for the Student class."""

    def __init__(self, first_name, last_name, age):
        """Descriptiojn for the initialization method."""
        self.first_name = first_name  # Attribue la valeur prénom à l’objet
        self.last_name = last_name  # Attribue la valeur nom à l’objet
        self.age = age  # Attribue la valeur âge à l’objet

    def to_json(self, attrs=None):
        """Returns the dictionary representation of the Student."""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            # Si attrs est une liste de chaînes
            my_dict = {}
            # Dictionnaire pour stocker les attributs sélectionnés
            for x in attrs:
                # Pour chaque nom dans la liste
                if hasattr(self, x):
                    # On vérifie que l'attribut existe dans l'objet
                    my_dict[x] = getattr(self, x)
                    # On récupère sa valeur et on l'ajoute au dictionnaire
            return my_dict
            # On retourne le dictionnaire avec les attributs sélectionnés

        return self.__dict__
        # Sinon, on retourne tous les attributs de l'objet
