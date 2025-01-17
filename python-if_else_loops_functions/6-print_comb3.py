#!/usr/bin/python3
for numero1 in range(0, 10):
    for numero2 in range(numero1 + 1, 10):
        if numero1 != 8 or numero2 != 9:
            print("{}{}".format(numero1, numero2), end=", ")
        else:
            print("{}{}".format(numero1, numero2))
