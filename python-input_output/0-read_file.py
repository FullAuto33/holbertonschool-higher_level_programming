#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read file"""
    with open(filename, encoding="utf-8") as f:
        # ouvre le fichier en mode lecture
        text = f.read()  # Lire le fichier
    print(text, end="")  # Afficher le texte lu
