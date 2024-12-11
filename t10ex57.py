def elements_parells(llista):
    return [llista[i] for i in range(len(llista)) if i % 2 == 0]

# Provar la funció
llista_prova = ["gato", "perro", "caballo", "vaca", "oveja", "gallina"]
resultat = elements_parells(llista_prova)
print(f"Llista original: {llista_prova}")
print(f"Paraules en posicions parells: {resultat}")