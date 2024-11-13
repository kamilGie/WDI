# ====================================================================================================>
# Zadanie 109
# Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która
# wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
# podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę
# maksymalnego podciągu.
# ====================================================================================================>
# return max_dlugosci


def Zadanie_109(tab):
    n = len(tab)
    res = suma = 0

    for y in range(n):
        for x in range(n):
            for i in range(1, 11):

                if i + y < n:
                    suma = 0
                    for j in range(y, i + y + 1):
                        suma += tab[j][x]
                    res = max(res, suma)

                if i + x < n:
                    suma = 0
                    for j in range(x, i + x + 1):
                        suma += tab[y][j]
                    res = max(res, suma)
    return res


