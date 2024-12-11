def comprovar_edad(edat):
    if edat > 18:
        return "És major d'edat."
    elif edat == 18:
        return "Té exactament 18 anys."
    else:
        return "No és major d'edat."

# Provar la funció
def main():
    edat = int(input("Introduïu la vostra edat: "))
    resultat = comprovar_edad(edat)
    print(resultat)

if __name__ == "__main__":
    main()