#!/usr/bin/python3
"""Description for the module."""


class Student:
    """Class student."""
    def __init__(self, first_name, last_name, age):
        """Public instance"""
        self.first_name = first_name  # Attribut le prenom
        self.last_name = last_name  # Attribut le nom
        self.age = age  # Attribut l'age

    def to_json(self, attrs=None):
        """json of student class"""
        if type(attrs) is list:
            # Verifie si attrs est une liste
            new_dict = {}  # Initialise un dictionnaire vide
            for key in self.__dict__:
                # Parcours les cles de l'instance
                for key2 in attrs:
                    # Parcours les cles de attrs
                    if key == key2:
                        # Si la cle de l'instance est dans attrs
                        new_dict[key] = self.__dict__[key]
                        # Ajoute la cle et sa valeur au dictionnaire
            return new_dict
            # Sinon retourne le dictionaire
        else:
            # Si attrs n'est pas une liste
            return self.__dict__
        # Retourne le dictionnaire de l'instance

    def reload_from_json(self, json):
        """Update json of student class"""
        self.__dict__.update(json)
        # Met a jour les attributs de l'instance
