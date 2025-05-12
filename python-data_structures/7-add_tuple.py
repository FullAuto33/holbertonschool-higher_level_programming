#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples."""
    if len(tuple_a) < 2:  # Si la longueur de tuple_a est inférieure à 2
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
        # On ajoute des zéros à la fin de tuple_a
        # pour qu'il ait une longueur de 2
    if len(tuple_b) < 2:  # Si la longueur de tuple_b est inférieure à 2
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
        # On ajoute des zéros à la fin de tuple_b
        # pour qu'il ait une longueur de 2
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    # On retourne la somme des deux tuples
