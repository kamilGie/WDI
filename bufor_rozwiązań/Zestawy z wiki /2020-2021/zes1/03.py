szukana_liczba = int(input())

a1, a2 = 1, 1
b1, b2 = 1, 1
suma = 0
while a1 < szukana_liczba:
    suma += a1
    while suma > szukana_liczba:
        suma -= b1
        b1, b2 = b2, b1+b2

    if suma == szukana_liczba:
        print(True)
        break

    a1, a2 = a2, a1+a2


if suma != szukana_liczba:
    print(False)


