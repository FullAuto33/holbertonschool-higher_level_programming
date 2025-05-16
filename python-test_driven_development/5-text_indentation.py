#!/usr/bin/python3
""" prints a text with 2 new lines after characters: ., ? and :"""


def text_indentation(text):
    """ prints a text with 2 new lines after characters: ., ? and :"""
    if not isinstance(text, str):  # Verifie si text est une chaîne
        raise TypeError("text must be a string")  # Retourne TypeError
    new_text = ""  # Initialise une nouvelle chaîne
    for i in range(len(text)):  # Pour chaque caractère de la chaîne
        new_text += text[i]  # Ajoute le caractère à la nouvelle chaîne
        if text[i] in ".?:":  # Si le caractère est ., ? ou :
            new_text += "\n\n"  # Ajoute deux nouvelles lignes
    print(new_text.strip(), end="")  # Affiche la nouvelle chaîne sans espaces vides
