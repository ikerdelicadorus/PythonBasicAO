def index_paraula(llista, paraula):
    try:
        return llista.index(paraula)
    except ValueError:
        return -1

# Provar la funció
llista_ordenada = ["a", "ametlla", "banana", "cirera", "dàtil", "figa", "llimona", "maduixa"]
paraula = "cirera"
index = index_paraula(llista_ordenada, paraula)
print(f"L'índex de la paraula '{paraula}' és: {index}")

paraula = "poma"
index = index_paraula(llista_ordenada, paraula)
print(f"L'índex de la paraula '{paraula}' és: {index}")