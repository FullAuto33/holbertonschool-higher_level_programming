#!/usr/bin/python3
def no_c(my_string):
    char = ""
    for i in my_string:
        if i != "C" and i != "c":
            char += i
    return (char)
