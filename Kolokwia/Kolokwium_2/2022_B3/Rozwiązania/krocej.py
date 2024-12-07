# ====================================================================================================>
# Zadanie B3, 15.12.2022
# Na szachownicy o wymiarach N × N umieszczono pewną liczbę pionków. Położenie pionków opisuje
# lista [(w0, k0),(w1, k1),(w2, k2), ...]. W lewym górnym rogu szachownicy (o współrzędnych 0, 0) znajduje się
# wieża, która musi dotrzeć do prawego dolnego rogu szachownicy. Wieża może wykonywać ruchy w prawo lub
# w dół szachownicy i nie może zbijać pionków. Proszę napisać funkcję rook(N,L), która zwróci minimalną
# liczbę ruchów jakie musi wykonać wieża aby dotrzeć do celu. Do funkcji należy przekazać wyłącznie dwa
# parametry: rozmiar szachownicy N oraz listę L zawierającą położenia pionków. Jeżeli dotarcie do celu nie
# jest możliwe funkcja powinna zwrócić wartość None.
#  ====================================================================================================>

from math import inf


def rook(N, L):
    def ruch(x, y, prev_move=None):
        if not (0 <= x < N and 0 <= y < N) or (x, y) in L:
            return inf
        if (x, y) == (N - 1, N - 1):
            return 0
        return min(
            ruch(x, y + 1, "p") + (prev_move != "p"),
            ruch(x + 1, y, "d") + (prev_move != "d"),
        )

    return None if (res := ruch(0, 0)) == inf else res
