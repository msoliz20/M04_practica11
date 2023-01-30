def nombres(nombre):
    lista = ["Pablo", "Pedro", "Jose", 'Miguel', "Javier"]
    if lista[0] == nombre:
        a = "Has escogido a Pablo"
    if lista[1] == nombre:
        a = "Has escogido a Pedro"
    if lista[2] == nombre:
        a = "Has escogido a Jose"
    if lista[3] == nombre:
        a = "Has escogido a Miguel"
    if lista[4] == nombre:
        a = "Has escogido a Javier"
    else:
        print("Este nombre no está en la lista")
    return a
