# ====================================================================================================>
# Zadanie 39
# Napisać program, który wyznacza liczbę zer jakimi kończy się liczba N! Program powinien
# działać dla N rzędu 10100.
# ====================================================================================================>
# zadanie_39(26) -->return 6

from math import factorial


def Zadanie_39(N):
    liczba_zer = 0

    silnia, d = divmod(factorial(N), 10)
    while d == 0:
        liczba_zer += 1
        silnia, d = divmod(silnia, 10)

    return liczba_zer


