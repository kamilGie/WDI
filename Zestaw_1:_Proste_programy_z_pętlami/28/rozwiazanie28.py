# ====================================================================================================>
# Zadanie 28
# Proszę napisać program wczytujący liczbę naturalną i rozkładający ją na iloczyn 2 liczb o
# najmniejszej różnicy. Na przykład: 30=5∗6, 120=10∗12.
# ====================================================================================================>

from math import isqrt


def Zadanie_28(n):
    i = isqrt(n)
    while i > 1:
        if n % i == 0:
            break
        i -= 1

    return i, n // i
