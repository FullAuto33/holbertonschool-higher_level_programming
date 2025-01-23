#!/usr/bin/python3
def multiple_returns(sentence):
    taille = len(sentence)
    if not sentence:
        return (taille, None)
    else:
        return (taille, sentence[0])
