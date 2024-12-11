"""
Definir una funció es_palindrom() que retorni vertader si li passem un palíndrom i 
fals en cas contrari. Un palíndrom és una paraula que s’escriu igual d’esquerra a dreta i 
de dreta a esquerra. 
Per exemple: radar, ara, civic, rallar, tapat, simis, refer, ...
"""

def invertir(s):
    return s[::-1]

def es_palindrom(s):
    if s == invertir(s):
        return True
    else:
        return False
    
s = input("Introdueixi una cadena: ")
a = invertir(s)
if es_palindrom(s):
    print("La frase/paraula {} és igual a {} i, per tant, és palíndrom".format(s, a))
else:
    print("La frase/paraula {} no és igual a {} i, per tant, no és palindrom".format(s, a))