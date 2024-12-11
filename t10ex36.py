import random
import time

# Funció on expliquem què passa
def intro():
    print ("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar,
    Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.
    Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran
    i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.
    """)

# Funció on demanem a quin talaiot volem anar
def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

# Funció que ens indica si compartiran el menjar o serem nosaltres el seu àpat
def trobada(canviTalaiot):
    print ("T'estas apropant al talaiot...")
    time.sleep(2)
    print ("Està fosc i és tenebrós...")
    time.sleep(2)
    print ("Un gran gegant salta davant teu, t'agafa i ...")
    print ("")
    time.sleep(2)
    gegantamic = random.randint (1, 2)
    if canviTalaiot == str(gegantamic):
        print ("Et convida a menjar...")
        return True
    else:
        print ("Se't menja d'un mos...ÑAMÑAMÑAM")
        return False

# Funció principal
def main():
    punts = 0
    partidaNova = "si"
    while partidaNova == "s" or partidaNova == "si":
        intro()
        nTalaiot = canviTalaiot()
        guanyat = trobada(nTalaiot)
        if guanyat:
            punts += 1
        else:
            break
        partidaNova = input("Vols tornar a jugar (si o no): ")
        print("\n")
    
    print(f"Has aconseguit {punts} punts.")

if __name__ == "__main__":
    main()