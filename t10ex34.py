def comptar_vocals(paraula):
    vocals = 'aeiou'
    comptador = {vocal: 0 for vocal in vocals}
    
    for lletra in paraula.lower():
        if lletra in comptador:
            comptador[lletra] += 1
    
    return comptador

def mostrar_resultat(comptador):
    resultat = []
    for vocal, quantitat in comptador.items():
        resultat.append(f"{quantitat} {vocal}'s")
    
    return ", ".join(resultat)

# Provar la funció
paraula = "Ratapinyada"
comptador = comptar_vocals(paraula)
resultat = mostrar_resultat(comptador)
print(f"A la paraula '{paraula}', {resultat}.")