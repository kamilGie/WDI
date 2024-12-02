# ====================================================================================================>
# Zadanie 97
# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
# tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
# powinny zawierać zera.
# ====================================================================================================>
# return tablica T2

# https://github.com/MarcinSerafin03/bit-algo-start-24-25-WDI/tree/main


def Zadanie_97(T1):
    N = len(T1)
    Indexes_Table = [0 for _ in range(N)]
    T2_index = 0
    T2 = [0 for _ in range(N * N)]

    while True:
        smallest = float("inf")
        is_singleton = False
        for i in range(N):
            if Indexes_Table[i] >= N:
                continue
            if smallest == T1[i][Indexes_Table[i]]:
                is_singleton = False
            elif smallest > T1[i][Indexes_Table[i]]:
                smallest = T1[i][Indexes_Table[i]]
                is_singleton = True

        if is_singleton:
            print(f"found singleton {smallest}")  # debuging purposes
            T2[T2_index] = smallest
            T2_index += 1

        if smallest == float("inf"):
            break

        for i in range(N):
            if Indexes_Table[i] >= N:
                continue
            if smallest == T1[i][Indexes_Table[i]]:
                Indexes_Table[i] += 1

    return T2
