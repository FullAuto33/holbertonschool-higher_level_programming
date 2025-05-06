#!/usr/bin/python3
def pow(a, b):
    """Calculate a to the power of b."""
    if b == 0:
        return 1
    elif b < 0:
        return 1 / (a ** -b)
    else:
        return a ** b
