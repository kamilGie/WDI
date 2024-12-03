# ====================================================================================================>
# Zadanie 66
# Napisać program wypełniający N-elementową tablicę T liczbami pseudolosowymi z zakresu
# 1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.
# ====================================================================================================>
# Funkcja list_check bedzie sprawdzac czy ta tablica ma conajmniej 1 element z cyframi nieparzystami
# Generowanie nie bedzie podlegac testa i moze byc zaimplemenotwane gdzie chcesz


from random import randint


def is_all_odd_number(n):
    while n > 0:
        if (n % 10) % 2 == 0:
            return False
        else:
            n = n // 10

    return True


def list_check(tab):
    for el in tab:
        if is_all_odd_number(el):
            return True

    return False


if __name__ == "__main__":

    n = int(input())
    tab = [randint(1, 1000) for _ in range(0, n)]
    list_check(tab)

