import random

def generar_codi():
    return [random.randint(0, 9) for _ in range(4)]

def comprovar_codi(codi, intent):
    encerts_posicio = 0
    encerts_numeros = 0
    
    codi_copia = codi[:]
    intent_copia = intent[:]
    
    # Comprovar els encerts en la posició correcta
    for i in range(4):
        if intent[i] == codi[i]:
            encerts_posicio += 1
            codi_copia[i] = -1
            intent_copia[i] = -2
    
    # Comprovar els encerts de nombres
    for i in range(4):
        if intent_copia[i] != -2:
            if intent_copia[i] in codi_copia:
                encerts_numeros += 1
                codi_copia[codi_copia.index(intent_copia[i])] = -1
    
    return encerts_posicio, encerts_numeros

def main():
    codi = generar_codi()
    encertat = False
    
    print("Benvingut a MasterMind! Intenta endevinar el codi de 4 xifres.")
    
    while not encertat:
        intent = input("Introduïu un codi de 4 xifres: ")
        intent = [int(x) for x in intent]
        
        encerts_posicio, encerts_numeros = comprovar_codi(codi, intent)
        
        if encerts_posicio == 4:
            encertat = True
            print("Felicitats! Has endevinat el codi!")
        else:
            print(f"Encerts a la posició correcta: {encerts_posicio}")
            print(f"Encerts de números (fora de posició): {encerts_numeros}")
    
if __name__ == "__main__":
    main()