# ====================================================================================================>
# Zadanie 98
# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów:T1[N][N]iT2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
# T2 były uporządkowane niemalejąco.
# ====================================================================================================>

# z wiki ale nie wymysle narazie testow


def singletony(T1, T2):
    n = len(T1)
    for v in range(n):  # wiersze w tablicy T1
        for element in T1[v]:  # elementy wiersza i-tego tablicy
            flag = True
            i = 0
            while i < n * n:
                if T2[i] <= element:
                    flag = False
                    break
                # end if
                i += 1
            # end while
            if flag:
                T2.append(element)
        # end for 2
    # end for 1
    return T2


if __name__ == "__main__":
    from Develop import stworz_zadanie

    stworz_zadanie([singletony])
