# ====================================================================================================>
# Zadanie 62
# Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Era-
# tostenesa.
# ====================================================================================================>
# print(pierwsza,end=" ")
# erastotenes(20) -> print(2 3 5 7 11 13 17,19)


from math import isqrt


def eratostenes(n):
    t = [True for _ in range(n + 1)]
    t[0] = t[1] = False

    for i in range(2, isqrt(n) + 1):
        if t[i]:
            for j in range(i * i, n + 1, i):
                t[j] = False

    for i in range(n):
        if t[i]:
            print(i, end=" ")


