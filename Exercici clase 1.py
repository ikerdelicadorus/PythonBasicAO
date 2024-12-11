a="Hola"
b= input("Llegir paraula: ")
#Mostri carcters de la paraula llegida
for e in b: 
    peint(e)
# Longitud paraula
print(len(b))

# Comprar-les
if a == b:
    prinnt("{} i {} són iguals ".format(a,b))
else:
    print("{} i {} són diferents".format(a, b))

# juntar-les amb un guió
print(a+"-"+b)

# Repetir-la 3 vegadas
print(b*3)

#Mirar si la vocal a és dins b(string)
if "a" in b:
    print("a és dins l'string {}".format(b))
