#!/usr/bin/python3
"""Prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>"""
    if not isinstance(first_name, str):  # Verifie si first_name est une chaîne
        raise TypeError("first_name must be a string")  # Retourne TypeError
    if not isinstance(last_name, str):  # Verifie si last_name est une chaîne
        raise TypeError("last_name must be a string")  # Retourne TypeError
    print(f"My name is {first_name} {last_name}")  # Affiche le nom
