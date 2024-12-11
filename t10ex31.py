def mostrar_majors_que(numbers, limit):
    # Filtrar els números que són majors que el límit
    majors = [num for num in numbers if num > limit]
    
    # Imprimir els números majors que el límit
    for num in majors:
        print(num)

def main():
    # Permetre a l'usuari introduir els valors enters de la tupla
    values = input("Introduïu els valors enters de la tupla, separats per comes: ")
    # Convertir els valors a una tupla de números enters
    numbers = tuple(map(int, values.split(',')))
    
    # Definir el límit per comprovar (18 anys)
    limit = 18
    
    # Mostrar els números majors que el límit
    print(f"Els números majors de {limit} són:")
    mostrar_majors_que(numbers, limit)

if __name__ == "__main__":
    main()