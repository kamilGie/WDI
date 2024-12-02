# ====================================================================================================>
# Zadanie 98
# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów:T1[N][N]iT2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
# T2 były uporządkowane niemalejąco.
# ====================================================================================================>
# return T2 uporzadkowane


def Zadanie_98(T1, T2):
    indeks_T2 = 0  # Początkowy indeks dla T2
    for tab in T1:
        for element in tab:
            k = indeks_T2 - 1
            while k >= 0 and T2[k] > element:
                T2[k + 1] = T2[k]
                k -= 1
            T2[k + 1] = element
            indeks_T2 += 1

    return T2


