"""
Definir una funció que utilitzi crear_punts() i dibuixi una imatge per la pantalla.


"""
def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l
def crear_punts(l):
    s="."
    for e in l:
        print("{} \n".format(s*e))
        s="."
#Programa principal
a = llegir_llista()
b=llegir_llista()
crear_punts(a)
crear_punts(b)
crear_punts(a)