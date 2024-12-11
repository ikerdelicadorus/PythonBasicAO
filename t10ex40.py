def suma_quadrats(n):
    suma = 0
    for i in range(n, 0, -4):
        suma += i ** 2
    return suma

def main():
    while True:
        try:
            n = int(input("Introduïu un número menor de 100: "))
            if n >= 100:
                raise ValueError("El número ha de ser menor de 100.")
            break
        except ValueError as e:
            print(e)
            print("Si us plau, torneu-ho a provar.\n")
    
    resultat = suma_quadrats(n)
    print(f"La suma dels quadrats dels números separats per quatre posicions des de {n} és: {resultat}")

if __name__ == "__main__":
    main()