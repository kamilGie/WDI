# ====================================================================================================>
# Zadanie 65
# Napisać program wypełniający N-elementową tablicę T liczbami naturalnymi 1-1000 i sprawdzający
# czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
# ====================================================================================================>
# Funkcja list_check bedzie sprawdzac czy ta tablica ma conajmniej jedna cyfre nieparzysta
from random import randint


def list_check(tab): ...


if __name__ == "__main__":
    from testy65 import odpal_testy

    n = int(input())
    tab = [randint(1, 1000) for _ in range(0, n)]
    list_check(tab)

    # odpal_testy()
