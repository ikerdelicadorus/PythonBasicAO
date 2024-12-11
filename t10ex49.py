import random

def llista_20_elements():
    return [random.randint(1, 100) for _ in range(20)]

def hi_ha_duplicats(llista):
    return len(llista) != len(set(llista))

# Provar les funcions
llista = llista_20_elements()
print(f"Llista generada: {llista}")
duplicats = hi_ha_duplicats(llista)
print(f"Hi ha elements duplicats a la llista? {duplicats}")