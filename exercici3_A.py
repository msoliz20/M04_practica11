import random


def numAleatorio(a):
    b = random.randrange(0, 100)
    if a == b:
        valor = "Molt bé! Has endevinat el número!"
    if a < b:
        valor = "El número és més gran"
    else:
        valor = "El número és més petit"
    return valor


