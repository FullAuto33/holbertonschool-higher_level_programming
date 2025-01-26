#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        result = a_dictionary.get(i)
        print('{}: {}'.format(i, result))
