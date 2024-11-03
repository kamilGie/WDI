# ====================================================================================================>
# Zadanie 31
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3*(An-1) +1, a pierwszy wyraz jest
# równy 2.
# ====================================================================================================>


def czy_ciag(n):
    an = 2
    while an <= n:
        if n % an == 0:
            return True
        an = 3 * an + 1

    return False


