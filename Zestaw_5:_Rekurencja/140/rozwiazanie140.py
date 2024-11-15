# ====================================================================================================>
# Zadanie 140
# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe
# odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
# ====================================================================================================>
# return bool


def waga(
    li, n, p=0
):  # li - lista odważników, n - szukana waga, p - numer branego odważnika
    if n == 0:
        return True
    if p == len(li):
        return False
    return waga(li, n - li[p], p + 1) or waga(li, n, p + 1)


def Zadanie_140(T, okreslona_masa):
    return waga(T, okreslona_masa)


