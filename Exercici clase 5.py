def llegir_llista():
    l=[]
    a="1"
    while a!=".":
        a = input("Introdueixi un caràcter diferent a .: ")
        if a!=".":
            l.append(a)
        else:
            print("Adéu!")
    return l

def elements_llista(l):
    d=dict()
    c="abcdefgjijklmnñopqrstuwxyzABCDEFGHIJKLMNÑOPQRSTUWXYZ"
    for e in c:
        d[e]=0
    return d


#programa principal
p = llegir_llista()
print(p)
d= elements_llista(l)
print(d)