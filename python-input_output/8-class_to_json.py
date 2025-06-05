#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """Class to JSON"""
    resultat = {}
    if hasattr(obj, "__dict__"):
        resultat = obj.__dict__
    return resultat
