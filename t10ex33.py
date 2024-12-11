def nums_que_comencen_per(noms, lletra):
    # Filtrar noms que comencen per la lletra donada
    comencen_per = [nom for nom in noms if nom.lower().startswith(lletra.lower())]
    # Retornar el nombre de noms que comencen per la lletra
    return len(comencen_per)

def main():
    # Llista de noms per provar
    noms = ["Anna", "Pere", "Arnau", "Maria", "Aina", "Joan"]
    
    # Demanar la lletra a l'usuari
    lletra = input("Introduïu la lletra per buscar: ").lower()
    
    # Mostrar el nombre de noms que comencen per la lletra
    resultat = nums_que_comencen_per(noms, lletra)
    print(f"Hi ha {resultat} noms que comencen per la lletra '{lletra}'.")

if __name__ == "__main__":
    main()