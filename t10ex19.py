"""
Definir una funció invertir() que calculi la inversa d’una cadena. 
Ex: invertir(“Soc del Ramis”) hauria de tornar la cadena “simaR led coS”.
"""

def invertir(s):
    return s[::-1]
s = input("Introdueixi una cadena: ")
print("La inversa de {} és {}".format(s, invertir(s)))