def crear_llista_fitxer(nom_fitxer):
    llista = []
    try:
        with open(nom_fitxer, 'r') as fitxer:
            for linia in fitxer:
                paraules = linia.split()
                llista.extend(paraules)
    except FileNotFoundError:
        print(f"El fitxer {nom_fitxer} no existeix.")
    return llista

# Provar la funció
nom_fitxer = 'exemple.txt'
llista_paraules = crear_llista_fitxer(nom_fitxer)
print(f"Llista de paraules del fitxer {nom_fitxer}: {llista_paraules}")