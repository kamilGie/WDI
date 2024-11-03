# ====================================================================================================>
# Zadanie 44
# Liczbę pierwszą będącą palindromem nazywamy “palindromem pierwszym”. Liczbę nazywamy “super palindromem pierwszym”
# jeżeli podczas odrzucania parami skrajnych cyfr do końca pozostaje ona palindromem pierwszym.
# Na przykład, liczba 373929373 jest super palindromem pierwszym bo 373929373,7392937,39293,929,2
# są palindromami pierwszymi.Początkowymi super palindromami pierwszymi są:
# 2,3,5,7,11,131,151.Proszę napisać program,który wylicza ile jest super palindromów pierwszych
# mniejszych od zadanej liczby n.
# =================================================================================== =================>
# to jest to samo co zadanie 24


from math import sqrt


def isprime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False

    for i in range(7, int(sqrt(n) + 1), 6):
        if n % i == 0:
            return False
    return True


def Zadanie_44(N):
    def nowe_brzegi(srodek, dlugosci):
        for i in range(10):
            nowy_srodek = (10**dlugosci * i + srodek) * 10 + i
            if nowy_srodek < N and isprime(nowy_srodek):
                print(nowy_srodek)
                nowe_brzegi(nowy_srodek, dlugosci + 2)

    for i in range(min(N, 10)):
        if isprime(i):
            print(i)
            nowe_brzegi(i, 1)

    for i in range(10, min(N, 100)):
        if i % 10 == i // 10 and isprime(i):
            print(i)
            nowe_brzegi(i, 2)
