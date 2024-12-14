# ====================================================================================================>
# Zadanie 117
# W tablicy o rozmiarze NxN wypełnionej liczbami naturalnymi umieszczono dokładnie jeden
# fragment ciągu Fiboacciego o długości co najmniej 3 elementów. Ciąg ten może leżeć w tablicy pionowo lub
# poziomo w kierunku rosnącym lub malejącym. Proszę napisać funkcje, która dla zadanej tablicy od szuka ten
# fragment i zwróci jego długość.
# ====================================================================================================>


def czy_podciag_fibo(n1, n2, n3):
    a, b = 1, 0
    while n3 > a + b:
        a, b = a + b, a
    return n1 == b and n2 == a and n3 == a + b


def Podciag_fibo(s):
    for i in range(len(s) - 2):
        if czy_podciag_fibo(s[i], s[i + 1], s[i + 2]):
            res = 3
            while i + res < len(s) and s[i + res - 2] + s[i + res - 1] == s[i + res]:
                res += 1
            return res
    return 0


def Zadanie_117(T):
    transpozycja_T = [list(row) for row in zip(*T)]
    for i in range(len(T)):
        if ( res := max( Podciag_fibo(T[i]), Podciag_fibo(T[i][::-1]), Podciag_fibo(transpozycja_T[i]), Podciag_fibo(transpozycja_T[i][::-1]),)) > 2:
            return res
