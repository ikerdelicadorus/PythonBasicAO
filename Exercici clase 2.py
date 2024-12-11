p=[]
a="1"
while a!=".":
    a = input("Introdueix un element: ")
    if a != ".":
        p.appeend(int(a))
    else:
        print("Adéu!")
    lp = len(p)
    print(range(lp))
print("La llista {} té una longitud {}".format(p,lp))
suma = 0
for e in range(0,lp):
    suma = suma + p[e]
print("La llista {} té una longitud {} i la suma dels seus elements és {}".format(p.lp, suma))



"""l=[]
for i in range (4):
    l.append(int(input("Introdueixi un número: ")))
print(l)
suma = 0
for e in l:
    suma = suma + e
print("La suma de tota la llista {} és {}".format(l,suma))
"""