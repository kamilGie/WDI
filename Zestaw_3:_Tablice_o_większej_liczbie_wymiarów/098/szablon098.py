# ====================================================================================================>
# Zadanie 98
# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów:T1[N][N]iT2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
# T2 były uporządkowane niemalejąco.
# ====================================================================================================>
# return T2 uporzadkowane


def Zadanie_98(T1, T2): ...


if __name__ == "__main__":
    from testy098 import odpal_testy

    Zadanie_98(int(input('Podaj T1: ')), int(input('Podaj T2: ')))

    # odpal_testy()
