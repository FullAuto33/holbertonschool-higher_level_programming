#!/usr/bin/python3

def roman_to_int(roman_string):
    """ Function convert Romans to integer"""
    if roman_string is None or not isinstance(roman_string, str):
        # Si roman_string est None ou n'est pas une chaîne
        return 0  # Retourne 0
    else:  # Sinon
        romannumber = {  # Dictionnaire romannumber
            'I': 1,  # I = 1
            'V': 5,  # V = 5
            'X': 10,  # X = 10
            'L': 50,  # L = 50
            'C': 100,  # C = 100
            'D': 500,  # D = 500
            'M': 1000  # M = 1000
        }
        result = 0  # Initialisation de result à 0
        for char in roman_string:  # Pour chaque caractère dans roman_string
            if char not in romannumber:  # Si le caractère n'est pas dans romannumber
                return 0  # Retourne 0
            current_value = romannumber[char]  # Récupère la valeur actuelle
            result += current_value  # Ajoute la valeur actuelle
        return result
