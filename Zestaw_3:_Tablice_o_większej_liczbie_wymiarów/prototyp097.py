# ====================================================================================================>
# Zadanie 97
# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
# tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
# powinny zawierać zera.
# ====================================================================================================>
# return tablica T2

# to cos psuje testy bede sprawdzal czemu nie dzialaja testy z 2 tablicami
from math import inf


def find_row(T, ixs):
    result = 0
    for i in range(1, len(T)):
        if T[i][ixs[i]] < T[result][ixs[result]]:
            result = i
    # end for
    return result


def Zadanie_97(T1, T2):
    n = len(T1)
    ixs = [0 for _ in range(n)]
    prev = -1
    T2_ix = 0
    i = 0

    while i < n * n:
        row = find_row(T1, ixs)
        if T1[row][ixs[row]] != prev:
            prev = T2[T2_ix] = T1[row][ixs[row]]
            T2_ix += 1
        if ixs[row] == n - 1:
            T1[row][ixs[row]] = inf
        else:
            ixs[row] += 1
        i += 1
    # end while
    return T2


if __name__ == "__main__":
    from Develop import stworz_zadanie

    stworz_zadanie([Zadanie_97])
