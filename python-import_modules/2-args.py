#!/usr/bin/env python3
import sys
if __name__ == "__main__":
    compteur = len(sys.argv) - 1
    if compteur == 0:
        print("0 arguments.")
    elif compteur == 1:
        print("1 argument:")
    else:
        print(f"{compteur} arguments:")
    for i in range(compteur):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
