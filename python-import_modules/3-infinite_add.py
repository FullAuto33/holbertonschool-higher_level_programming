#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    somme = 0
    taille = len(sys.argv)
    for i in range(1, taille):
        somme = somme + int(sys.argv[i])
    print (somme)
