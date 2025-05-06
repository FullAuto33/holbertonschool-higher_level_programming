#!/usr/bin/python3
if __name__ == "__main__":
    """ Print all names defined by the compiled module hidden_4"""
    import hidden_4  # Import le module hidden_4
    for name in dir(hidden_4):  # Parcourt les noms définis par le module
        if name[:2] != "__":  # Si le nom ne commence pas par "__"
            print(name) # Affiche le nom
