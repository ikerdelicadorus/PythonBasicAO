def comptar_digits(numero):
    return len(str(numero))

def main():
    while True:
        try:
            numero = int(input("Introduïu un número (mínim 1 i màxim 900000): "))
            if numero < 1 or numero > 900000:
                raise ValueError("El número ha de ser entre 1 i 900000.")
            break
        except ValueError as e:
            print(e)
            print("Si us plau, torneu-ho a provar.\n")
    
    quantitat_digits = comptar_digits(numero)
    print(f"El número {numero} té {quantitat_digits} dígits.")

if __name__ == "__main__":
    main()