def suma_interval(a, b):
    if a > b:
        a, b = b, a  # Assegurar-se que a és menor o igual a b
    suma = sum(range(a, b + 1))
    return suma

def main():
    try:
        a = int(input("Introduïu el primer número: "))
        b = int(input("Introduïu el segon número: "))
        resultat = suma_interval(a, b)
        print(f"La suma de tots els números entre {a} i {b} és: {resultat}")
    except ValueError:
        print("Si us plau, introduïu números enters vàlids.")

if __name__ == "__main__":
    main()