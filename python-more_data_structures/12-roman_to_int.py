#!/usr/bin/python3
def roman_to_int(roman_string):
     if type(roman_string) is not str or roman_string is None:
        return 0
    chiffre = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    somme = 0
    for i in range(len(roman_string)):
        result = chiffre[roman_string[i]]
        if i + 1 < len(roman_string) and chiffre[roman_string[i + 1]] > result:
            somme -= result
        else:
            somme += result
    return somme
