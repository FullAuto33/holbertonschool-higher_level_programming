#!/usr/bin/env python3
"""Picker module serialization example"""
import pickle


class CustomObject:
    """Class CustomObject"""
    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name  # Attribut le nom
        self.age = age  # Attribut l'âge
        self.is_student = is_student  # Attribut si c'est un étudiant

    def display(self):
        """Affiche les attributs de l'objet."""
        print("Name:", self.name)  # Affiche le nom
        print("Age:", self.age)  # Affiche l'âge
        print("Is Student:", self.is_student)  # Affiche si c'est un étudiant

    def serialize(self, filename):
        """Serialize the object to a file."""
        with open(filename, "wb") as file:
            # Ouvre le fichier en mode binaire pour écriture
            pickle.dump(self, file)
            # Sérialise l'objet et l'écrit dans le fichier

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file."""
        try:
            with open(filename, "rb") as file:
                # Ouvre le fichier en mode binaire pour lecture
                return pickle.load(file)
                # Désérialise l'objet depuis le fichier
        except Exception:
            # Si une erreur se produit
            return None
            # Retourne non
