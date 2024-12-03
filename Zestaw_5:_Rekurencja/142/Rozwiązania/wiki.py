# ====================================================================================================>
# Zadanie 142
# Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.
# ====================================================================================================>
# return [odwaznik1,odwaznik2]


def waga2(li, n, res=[], p=0):
    if n == 0:
        return res
    if p == len(li):
        return False
    return (
        waga2(li, n - li[p], res + [li[p]], p + 1)
        or waga2(li, n, res, p + 1)
        or waga2(li, n + li[p], res + [-1 * li[p]], p + 1)
    )


def Zadanie_142(T, okreslona_masa):
    return waga2(T, okreslona_masa)


