# ====================================================================================================>
# Zadanie 45
# Dane są dwie liczby naturalne, m i n. Proszę napisać program, który wyznacza sumę n
# kolejnych cyfr po przecinku rozwinięcia dziesiętnego liczby sqrt(m)
# ====================================================================================================>

from math import sqrt


def Zadanie_45(m, n):

    rozwiniecie = int(sqrt(m) * 10**n)

    suma = 0
    for _ in range(n):
        rozwiniecie, d = divmod(rozwiniecie, 10)
        suma += d
    return suma


