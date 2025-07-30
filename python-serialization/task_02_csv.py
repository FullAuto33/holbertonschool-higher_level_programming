#!/usr/bin/env python3
"""Module convert CSV to JSON."""
import csv
import json


def convert_csv_to_json(filename):
    """Convert CSV file to JSON format."""
    try:
        with open(filename, "r") as file:
            # Ouvre le fichier CSV en mode lecture
            rows = list(csv.DictReader(file))
            # Convertit les lignes du CSV en une liste de dictionnaires

        with open("data.json", "w") as file:
            # Ouvre le fichier JSON en mode écriture
            json.dump(rows, file)
            # Écrit les données JSON dans le fichier

        return True
        # Si tout se passe bien, retourne True
    except Exception:
        # En cas d'erreur
        return False
        # on retourne False
