def elimina_duplicats(llista):
    nova_llista = list(dict.fromkeys(llista))
    return nova_llista

# Provar la funció
llista_prova = [1, 2, 2, 3, 4, 4, 5]
nova_llista = elimina_duplicats(llista_prova)
print(f"Llista original: {llista_prova}")
print(f"Nova llista (sense duplicats): {nova_llista}")