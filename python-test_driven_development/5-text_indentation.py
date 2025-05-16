#!/usr/bin/python3
""" prints a text with 2 new lines after characters: ., ? and :"""


def text_indentation(text):
    """ prints a text with 2 new lines after characters: ., ? and :"""
    if not isinstance(text, str):  # Verifie si text est une chaîne
        raise TypeError("text must be a string")  # Retourne TypeError
    compteur = 0
    while compteur < len(text):
        print(text[compteur], end="")
        if text[compteur] in ".?:":
            print("\n")
            compteur += 1
            # Sauter les espaces après la ponctuation
            while compteur < len(text) and text[compteur] == " ":
                compteur += 1
            continue
        compteur += 1
