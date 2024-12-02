# ====================================================================================================>
# Zadanie 65
# Napisać program wypełniający N-elementową tablicę T liczbami naturalnymi 1-1000 i sprawdzający
# czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
# ====================================================================================================>
# Funkcja list_check bedzie sprawdzac czy ta tablica ma conajmniej jedna cyfre nieparzysta
# Generowanie nie bedzie podlegac testa i moze byc zaimplemenotwane gdzie chcesz
# list_check([1, 1, 1]) - > return True

from random import randint


def is_odd_number(n):
    while n > 0:
        if (n % 10) % 2 == 1:
            return True
        else:
            n = n // 10

    return False


def list_check(tab):
    for el in tab:
        if not is_odd_number(el):
            return False

    return True


if __name__ == "__main__":
    n = int(input())
    tab = [randint(1, 1000) for _ in range(0, n)]
