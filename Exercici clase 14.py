#Ex. Multiplicar per 3 tots els elemnts d'una llista
l=[2, 3, 4, 7, 10]

#Solució en bucle
r=[]
for e in l:
    r.append(e*3)
print(r)

#Solució utilitzant funció anonima(lambda) i map i (programacio funcional)
r=list(map(lambda x:x*3,l))
print(r)

#Solució utilizant ,map i una funció normal
def pertres(x):
    return x*3
r=llista(map(pertres,l))
print(r)

"""
#Examen. Donades dues paraules dir quina és més llarga
a=input("Escriure una paraula: ")
b=input("Escriure una paraula: ")
if len(a)>len(b):
    print("La paraula {} és major que la {}".format(a,b))
    print(f"La paraula {a} és major que la {b}")
elif len(b)>len(a):
    print("La paraula {} és major que la {}".format(b,a))
else:
    print("Són iguals")
"""