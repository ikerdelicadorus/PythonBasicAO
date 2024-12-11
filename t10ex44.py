def suma_digits(numero):
    suma = sum(int(digit) for digit in str(numero))
    return suma

def es_parell_o_senar(suma):
    if suma % 2 == 0:
        return "parell"
    else:
        return "senar"

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
    
    suma = suma_digits(numero)
    resultat = es_parell_o_senar(suma)
    print(f"La suma dels dígits de {numero} és {suma}, que és {resultat}.")

if __name__ == "__main__":
    main()
