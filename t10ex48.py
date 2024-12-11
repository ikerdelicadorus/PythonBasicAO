def hi_ha_duplicats(llista):
    return len(llista) != len(set(llista))

# Provar la funció
llista_prova1 = [1, 2, 3, 4, 5]
llista_prova2 = [1, 2, 3, 2, 5]

print(f"La llista {llista_prova1} té duplicats? {hi_ha_duplicats(llista_prova1)}")
print(f"La llista {llista_prova2} té duplicats? {hi_ha_duplicats(llista_prova2)}")