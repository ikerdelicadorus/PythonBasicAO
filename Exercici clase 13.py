def sumal(llista):
    ls=[]
    for e in llista:
        ls.append(e)
    return ls


#Programa principal
l = [2, 3, 4]
print(l)
s=suma(l)
print("La llista original és {} i la modificació {}".format(l, s))