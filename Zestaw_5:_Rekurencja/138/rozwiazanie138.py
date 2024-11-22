# ====================================================================================================>
# Zadanie 138
# Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w
# sensie liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów
# tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego
# podzbioru. Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.
# ====================================================================================================>

import math


def Zadanie_138(t):

    def rek(t, i, s_el=0, s_it=0, best=math.inf, l=0, s_best=0):
        if i >= len(t):
            return s_el == s_it and s_el > 0, s_el, l

        s_best = 0
        poss = False

        ans, s, leng = rek(t, i + 1, s_el, s_it, best, l)
        if ans and leng < best:
            best = leng
            s_best = s
            poss = True

        ans, s, leng = rek(t, i + 1, s_el + t[i], s_it + i, best, l + 1)
        if ans and leng < best:
            best = leng
            s_best = s
            poss = True

        return poss, s_best, best

    _, wynik, _ = rek(t, 0)

    return wynik
