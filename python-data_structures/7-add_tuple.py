#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lista = list(tuple_a)
    listb = list(tuple_b)
    while len(lista) < 2:
        lista.append(0)
    while len(listb) < 2:
        listb.append(0)
    result = [lista[0] + listb[0], lista[1] + listb[1]]
    return(tuple(result))
