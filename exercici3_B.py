def declaracio_impuestos():
    edat = int(input("Introdueix la teva edat: "))
    ingressos = int(input("Introdueix els teus ingressos mensuals: "))
    if edat >= 18 and ingressos > 1200:
        print("És necessari que facis la declaració d'impuestos")
    else:
        print("Encara no pots fer la declaració")
