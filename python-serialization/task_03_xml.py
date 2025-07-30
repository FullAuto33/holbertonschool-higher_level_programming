#!/usr/bin/env python3
"""Module convert XML to JSON."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""

    user = ET.Element("data")
    # Crée un élément racine XML

    for key, value in dictionary.items():
        # Pour chaque clé-valeur du dictionnaire
        child = ET.SubElement(user, key)
        # Crée un sous-élément XML pour chaque clé
        child.text = value
        # Définit le texte du sous-élément avec la valeur

    result = ET.ElementTree(user)
    # Crée un arbre XML à partir de l'élément racine
    result.write(filename, encoding="utf-8", xml_declaration=True)
    # Écrit l'arbre XML dans le fichier spécifié

def deserialize_from_xml(filename):
    """Deserialize an XML file to a dictionary"""

    result = ET.parse(filename)
    # analyse le fichier XML
    user = result.getroot()
    # Récupère l'élément racine de l'arbre XML

    result = {}
    # Initialise un dictionnaire vide pour stocker les données
    for child in user:
        # Pour chaque sous-élément de l'élément racine
        result[child.tag] = child.text
        # Ajoute la clé et la valeur au dictionnaire

    return result
    # Retourne le dictionnaire
