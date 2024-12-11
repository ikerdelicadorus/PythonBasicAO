def calcular_cfinal(cinicial, interes, anys):
    cfinal = cinicial * (1 + interes / 100) ** anys
    return cfinal

def main():
    while True:
        try:
            cinicial = float(input("Introduïu la quantitat a sol·licitar (mínim 50000€, màxim 800000€): "))
            if cinicial < 50000 or cinicial > 800000:
                raise ValueError("La quantitat ha de ser entre 50000€ i 800000€.")
            
            interes = float(input("Introduïu l'interès (mínim 0.5%, màxim 13%): "))
            if interes < 0.5 or interes > 13:
                raise ValueError("L'interès ha de ser entre 0.5% i 13%.")
            
            anys = int(input("Introduïu el número d'anys (mínim 3 anys, màxim 40 anys): "))
            if anys < 3 or anys > 40:
                raise ValueError("El número d'anys ha de ser entre 3 i 40 anys.")
            
            break
        except ValueError as e:
            print(e)
            print("Si us plau, torneu-ho a provar.\n")
    
    cfinal = calcular_cfinal(cinicial, interes, anys)
    print(f"El capital final després de {anys} anys serà de: {cfinal:.2f}€")

if __name__ == "__main__":
    main()