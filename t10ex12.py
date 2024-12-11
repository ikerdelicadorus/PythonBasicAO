def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacio(a, b):
    return a * b

def divisio(a, b):
    if b == 0:
        return "Error: divisió per zero."
    return a / b

def calculadora():
    print("Benvingut a la calculadora!")
    print("Operacions disponibles: suma, resta, multiplicació, divisió")
    
    while True:
        try:
            a = float(input("Introduïu el primer número: "))
            b = float(input("Introduïu el segon número: "))
            operacio = input("Introduïu l'operació (suma, resta, multiplicació, divisió): ").strip().lower()
            
            if operacio == "suma":
                resultat = suma(a, b)
            elif operacio == "resta":
                resultat = resta(a, b)
            elif operacio == "multiplicació":
                resultat = multiplicacio(a, b)
            elif operacio == "divisió":
                resultat = divisio(a, b)
            else:
                print("Operació no vàlida.")
                continue
            
            print(f"El resultat de {a} {operacio} {b} és: {resultat}")
        except ValueError:
            print("Si us plau, introduïu números vàlids.")

        continuar = input("Vols fer una altra operació? (si/no): ").strip().lower()
        if continuar != "si":
            break

if __name__ == "__main__":
    calculadora()