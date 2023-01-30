def numMayor(a, b):
    if a > b:
        valor = "El numero {a} es mayor que {b}".format(a=a, b=b)
    if a == b:
        print("El numero {a} es igual a {b}".format(a=a, b=b))
    else:
        valor = "El numero {b} es mayor que {a}".format(a=a, b=b)
    return valor
