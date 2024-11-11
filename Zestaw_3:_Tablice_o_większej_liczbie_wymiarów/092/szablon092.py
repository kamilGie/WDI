# ====================================================================================================>
# Zadanie 92
# Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
# naturalnymi po spirali.
# ====================================================================================================>
# return dwuwymiarowa tablica
# spirala(3) -> [[0, 1, 2], [7, 8, 3], [6, 5, 4]]


def spirala(n): ...


if __name__ == "__main__":
    from testy092 import odpal_testy

    spirala(int(input('Podaj n: ')))

    # odpal_testy()
