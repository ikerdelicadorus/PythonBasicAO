def imprimir_patron():
    # Primera part del patró
    for i in range(1, 4):
        print('*' * i)
    # Segona part del patró
    for i in range(2, 0, -1):
        print('*' * i)

if __name__ == "__main__":
    imprimir_patron()