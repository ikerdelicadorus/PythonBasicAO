def calcular_edad(any_actual, any_naixement):
    return any_actual - any_naixement

def main():
    any_actual = int(input("Introduïu l'any actual: "))
    
    noms = []
    anys_naixement = []
    
    for i in range(4):
        nom = input(f"Introduïu el nom de la persona {i + 1}: ")
        any_naixement = int(input(f"Introduïu l'any de naixement de {nom}: "))
        noms.append(nom)
        anys_naixement.append(any_naixement)
    
    print(f"{'Nom':<10}{'Data naixement':<20}{'Anys que farà aquest any':<25}")
    for i in range(4):
        edat = calcular_edad(any_actual, anys_naixement[i])
        print(f"{noms[i]:<10}{anys_naixement[i]:<20}{edat:<25}")

if __name__ == "__main__":
    main()