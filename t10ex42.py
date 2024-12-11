def imprimir_serie():
    for i in range(1, 16):
        print(i, end=" ")
    print()

def main():
    for _ in range(5):
        imprimir_serie()

if __name__ == "__main__":
    main()