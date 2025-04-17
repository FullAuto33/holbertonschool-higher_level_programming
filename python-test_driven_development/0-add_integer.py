#!/usr/bin/python3
def add_integer(a, b=98):
    if a not isinstance(int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    if b not isinstance(int) or not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b