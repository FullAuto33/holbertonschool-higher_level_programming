#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    nom = dir(hidden_4)
    for i in nom:
        if i[:2] != "__":
            print(i)
