#Funció que ens diu si un caràcter és o no una vocal
def esvocal(x):
    return x.lower() in "aeiou"
#programa principal
a = "a"
while(a!="."):
    a = input("Escriu la vocal")
    if esvocal(a):
        print("La lletra introduïda {} és vocal".format(a))
    else:
        print("La lletra introduïda {} no és una vocal".format(a))