def imprimir_patron():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()  # Nova línia després de cada sub-patró

if __name__ == "__main__":
    imprimir_patron()