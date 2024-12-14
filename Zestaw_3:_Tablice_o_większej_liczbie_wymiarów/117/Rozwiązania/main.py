# ====================================================================================================>
# Zadanie 117
# W tablicy o rozmiarze NxN wypełnionej liczbami naturalnymi umieszczono dokładnie jeden
# fragment ciągu Fiboacciego o długości co najmniej 3 elementów. Ciąg ten może leżeć w tablicy pionowo lub
# poziomo w kierunku rosnącym lub malejącym. Proszę napisać funkcje, która dla zadanej tablicy od szuka ten
# fragment i zwróci jego długość.
# ====================================================================================================>

# rozwiazanie zaklada ze umieszczono `DOKLADNIE JEDEN` fragment


def czy_podciag_fibo(n1, n2, n3):
    """sprawdzi czy 3 elementy sa nastepnymi elemetami ciagu fibo"""
    a, b = 1, 0
    while n3 > a + b:
        a, b = a + b, a

    return n1 == b and n2 == a and n3 == a + b


def Podciag_fibo(s):
    """zwraca dlugosci podciagu fibo jesli jest dluzszy niz 2"""
    n = len(s)
    for i in range(n - 2):
        if czy_podciag_fibo(s[i], s[i + 1], s[i + 2]):
            res = 3
            for j in range(i + 1, n - 2):
                if s[j] + s[j + 1] != s[j + 2]:
                    break
                res += 1

            return res
    return 0


def Zadanie_117(T):
    n = len(T)

    # transpozycja T dla slicow kolumny
    transpozycja_T = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transpozycja_T[j][i] = T[i][j]

    for i in range(n):
        wiersz = Podciag_fibo(T[i])
        if wiersz > 2:
            return wiersz

        wiersz_odwrotnie = Podciag_fibo(T[i][::-1])
        if wiersz_odwrotnie > 2:
            return wiersz_odwrotnie

        kolumna = Podciag_fibo(transpozycja_T[i])
        if kolumna > 2:
            return kolumna

        kolumna_odwrotnie = Podciag_fibo(transpozycja_T[i][::-1])
        if kolumna_odwrotnie > 2:
            return kolumna_odwrotnie


