def llegir_lllista():
    l=[]
    a="1"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":
            l.append(a)
        else:
            print("Adéu!")
    return l
#programa principal

l = llegir_llista()
cl = set(l)
if len(l)==len(cl):
    print("No hi ha cap paraula repetida")
else:
    print("N'hi ha de repetides, però encara no sé quines ")