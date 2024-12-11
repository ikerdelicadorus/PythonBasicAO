def convertir_base(numero, base_actual, base_destinacio):
    if base_actual == 10:
        numero_decimal = int(numero)
    elif base_actual == 2:
        numero_decimal = int(numero, 2)
    elif base_actual == 8:
        numero_decimal = int(numero, 8)
    elif base_actual == 16:
        numero_decimal = int(numero, 16)
    else:
        raise ValueError("Base actual no vàlida!")

    if base_destinacio == 10:
        return str(numero_decimal)
    elif base_destinacio == 2:
        return bin(numero_decimal)[2:]
    elif base_destinacio == 8:
        return oct(numero_decimal)[2:]
    elif base_destinacio == 16:
        return hex(numero_decimal)[2:]
    else:
        raise ValueError("Base destinació no vàlida!")

def operacions_basicas(num1, num2, operacio):
    if operacio == "+":
        return num1 + num2
    elif operacio == "-":
        return num1 - num2
    elif operacio == "*":
        return num1 * num2
    elif operacio == "/":
        return num1 / num2 if num2 != 0 else "Error: Divisió per zero!"
    else:
        return "Operació no vàlida!"

def menu():
    while True:
        print("\n--- Calculadora ---")
        print("1. Canviar base")
        print("2. Operacions matemàtiques")
        print("3. Sortir")
        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            numero = input("Introdueix el número: ")
            base_actual = int(input("Introdueix la base actual (2, 8, 10, 16): "))
            base_destinacio = int(input("Introdueix la base de destinació (2, 8, 10, 16): "))
            try:
                resultat = convertir_base(numero, base_actual, base_destinacio)
                print(f"El resultat és: {resultat}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcio == "2":
            try:
                num1 = float(input("Introdueix el primer número: "))
                num2 = float(input("Introdueix el segon número: "))
                operacio = input("Introdueix l'operació (+, -, *, /): ")
                resultat = operacions_basicas(num1, num2, operacio)
                print(f"El resultat és: {resultat}")
            except ValueError:
                print("Entrada no vàlida!")

        elif opcio == "3":
            print("Adéu!")
            break

        else:
            print("Opció no vàlida!")

if __name__ == "__main__":
    menu()
