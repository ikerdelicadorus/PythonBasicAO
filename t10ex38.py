def comprovar_rima(paraula1, paraula2):
    if paraula1[-3:] == paraula2[-3:]:
        return "Les paraules rimen completament."
    elif paraula1[-2:] == paraula2[-2:]:
        return "Les paraules rimen una mica."
    else:
        return "Les paraules no rimen."

# Programa principal
def main():
    paraula1 = input("Introduïu la primera paraula: ")
    paraula2 = input("Introduïu la segona paraula: ")
    
    resultat = comprovar_rima(paraula1, paraula2)
    print(resultat)

if __name__ == "__main__":
    main()