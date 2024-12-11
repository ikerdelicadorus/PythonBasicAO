def es_de_traspas(any):
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        return True
    else:
        return False

# Provar la funció
any = int(input("Introduïu un any per comprovar si és de traspàs: "))
if es_de_traspas(any):
    print(f"L'any {any} és de traspàs.")
else:
    print(f"L'any {any} no és de traspàs.")