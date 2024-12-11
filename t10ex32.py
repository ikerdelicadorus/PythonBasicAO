def nums_que_comencen_per(noms, lletra):
    # Filtrar noms que comencen per la lletra donada
    comencen_per = [nom for nom in noms if nom.lower().startswith(lletra.lower())]
    # Retornar el nombre de noms que comencen per la lletra
    return len(comencen_per)

# Provar la funció
noms = ["Anna", "Pere", "Arnau", "Maria", "Aina", "Joan"]
lletra = "a"
resultat = nums_que_comencen_per(noms, lletra)
print(f"Hi ha {resultat} noms que comencen per la lletra '{lletra}'.")