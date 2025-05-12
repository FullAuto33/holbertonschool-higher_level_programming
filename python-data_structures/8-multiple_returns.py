#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    if sentence == "":  # Si sentence est vide
        return (0, None)  # Renvoie 0 et None
    else:  # Sinon
        return (len(sentence), sentence[0])
        # Renvoie la longueur de la chaîne et son premier caractère
