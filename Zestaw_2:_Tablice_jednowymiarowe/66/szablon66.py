# ====================================================================================================>
# Zadanie 66
# Napisać program wypełniający N-elementową tablicę T liczbami pseudolosowymi z zakresu
# 1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.
# ====================================================================================================>
# Funkcja list_check bedzie sprawdzac czy ta tablica ma conajmniej 1 element z cyframi nieparzystami

from random import randint


def list_check(tab): ...


if __name__ == "__main__":
    from testy66 import odpal_testy

    n = int(input())
    tab = [randint(1, 1000) for _ in range(0, n)]
    list_check(tab)

    # odpal_testy()
