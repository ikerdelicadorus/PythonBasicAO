def imprimir_taula_multiplicar(numero):
    print(f"Taula de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()

def main():
    while True:
        try:
            numero = int(input("Introduïu un número (mínim 1 i màxim 20): "))
            if numero < 1 or numero > 20:
                raise ValueError("El número ha de ser entre 1 i 20.")
            break
        except ValueError as e:
            print(e)
            print("Si us plau, torneu-ho a provar.\n")
    
    imprimir_taula_multiplicar(numero)

if __name__ == "__main__":
    main()