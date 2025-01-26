#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = a_dictionary.copy()
    for i in result.keys():
        result[i] *= 2
    return result
