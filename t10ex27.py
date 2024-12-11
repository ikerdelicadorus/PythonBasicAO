"""
Definir una funció filtrar_paraules() que donada una llista de paraules i un número x, 
retorni totes les paraules que tingui més d’x-caràcters.
"""
def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":
            l.append(a)
    return l

def filtrar_paraules(l,n):
    return list(filter(lambda x:len(x)>n,l))

#Programa principal
x = llegir_llista()
y = int(input("Introdueixi un número: "))
print("De la llista {} que tinguin més de {}-caràcters hi ha {}".format(x,y,filtrar_paraules(x,y)))