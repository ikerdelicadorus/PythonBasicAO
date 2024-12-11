def digits_parells(numero):
    digits_parells = [int(digit) for digit in str(numero) if int(digit) % 2 == 0]
    return digits_parells

def main():
    while True:
        try:
            numero = int(input("Introduïu un número: "))
            if numero < 0:
                raise ValueError("El número ha de ser positiu.")
            break
        except ValueError as e:
            print(e)
            print("Si us plau, torneu-ho a provar.\n")
    
    parells = digits_parells(numero)
    print(f"Els dígits parells del número {numero} són: {parells}")

if __name__ == "__main__":
    main()