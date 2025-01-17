#!/usr/bin/python3
for nombre in range(0, 100):
    if nombre != 99:
        print("{:02}".format(nombre), end=", ")
    else:
        print(f"{nombre}")
