def eliminarcapicua(llista):
    if len(llista) < 2:
        return []  # Si la llista té menys de 2 elements, retornem una llista buida
    return llista[1:-1]

# Provar la funció
llista_prova = [1, 2, 3, 4, 5]
nova_llista = eliminarcapicua(llista_prova)
print(f"Llista original: {llista_prova}")
print(f"Nova llista (sense el primer i darrer element): {nova_llista}")