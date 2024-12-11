def es_primer(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primers_fins_a_100():
    primers = [n for n in range(2, 101) if es_primer(n)]
    return primers

def main():
    primers = primers_fins_a_100()
    print("Números primers entre 1 i 100:")
    print(primers)
    print(f"Hi ha {len(primers)} números primers entre 1 i 100.")

if __name__ == "__main__":
    main()