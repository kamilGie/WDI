# ====================================================================================================>
# Zadanie 97
# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
# tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
# powinny zawierać zera.
# ====================================================================================================>
# return tablica T2


def Zadanie_97(T1, T2): ...


if __name__ == "__main__":
    from testy097 import odpal_testy

    Zadanie_97(list(input("Podaj T1: ")), list(input("Podaj T2: ")))

    # odpal_testy()
