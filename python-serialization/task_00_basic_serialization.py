#!/usr/bin/env python3
"""Description module serialization basic"""

import json


def serialize_and_save_to_file(my_obj, filename):
    """Ecrit un objet Python dans un fichier JSON. serialization"""
    with open(filename, "w") as file:
        # Ouvre le fichier en mode écriture
        json.dump(my_obj, file)
        # Sérialise l'objet Python en JSON et l'écrit dans le fichier


def load_and_deserialize(filename):
    """Lit un fichier JSON et le désérialise en objet Python."""
    with open(filename, "r") as file:
        # Ouvre le fichier en mode lecture
        return json.load(file)
        # Désérialise le contenu JSON en objet Python et le retourne
