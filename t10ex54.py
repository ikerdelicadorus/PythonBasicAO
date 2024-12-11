#Numero parells
def mostrar_parells():
    for i in range(2, 101, 2):
        print(i, end=", " if i < 100 else "\n")

if __name__ == "__main__":
    mostrar_parells()
    
#Numeros senar
def mostrar_senars():
    for i in range(1, 100, 2):
        print(i, end=", " if i < 99 else "\n")

if __name__ == "__main__":
    mostrar_senars()
