# ====================================================================================================>
# Zadanie 29
# Proszę napisać programwczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An =n∗n+n+1.
# ====================================================================================================>


from math import isqrt


def czy_ciag(n):
    for i in range(1, isqrt(n) + 1):
        an = i * i + i + 1
        if n % an == 0:
            return True

    return False


