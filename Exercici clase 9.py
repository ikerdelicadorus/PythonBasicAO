a = int(input("Escriu un número: "))
b = int(input("escriu un número: "))
c = int(input("escriu un número: "))
if a > b:
    if b > c:
        print("{} és major que {} i aquest és major que {}".format(a,b,c))
    elif b<a:
        if a>c:
            print("{} és major que {} i aquest és major que {}".format(a,b,c))
        elif c>a:
            print("{} és major que {} i aquest és major que {}".format(a,b,c))
        else:
            print("{} i {} son iguals i major  major que {}".format(a,b,c))

