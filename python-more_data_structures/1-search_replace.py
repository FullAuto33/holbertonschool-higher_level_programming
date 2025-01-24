#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] == search:
            result[i] == replace
    return result
