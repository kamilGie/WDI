# ====================================================================================================>
# Zadanie 13
# Liczba doskonała to liczba równa sumie swoich podzielników właściwych (mniejszych od
# jej samej), na przykład 6 = 1+2+3. Proszę napisać program wyszukujący liczby doskonałe mniejsze od
# miliona.
# ====================================================================================================>


def dzielniki(n):
    i = 2
    suma = 1
    while i * i < n:
        if n % i == 0:
            suma += i + (n // i)
        i += 1

    if i * i == n:
        suma += i

    return suma


def Zadanie_13():
    for i in range(1, 1000001):
        if i == dzielniki(i):
            print(i, end=" ")


