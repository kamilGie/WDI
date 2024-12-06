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
    def legalne(x, y):
        return (0 <= x < N) and (0 <= y < N)

    def ruch(pos, prev_move=None):
        """zwroci minimalna ilosci ruchow lub inf jak sie nie da dotrzec z danej pozycji do mety"""
        if not legalne(pos[0], pos[1]):  # wyszlismy po za szachownice
            return inf
        if pos in L:  # pozycja pionka
            return inf
        if pos == (N - 1, N - 1):  # meta
            return 0

        # sprawdzam 2 mozliwosci ruchu z danej pozycji
        prawo = ruch((pos[0], pos[1] + 1), "prawo")
        dol = ruch((pos[0] + 1, pos[1]), "dol")

        # jesli skrecilem dodaj to do ruchow
        if prev_move != "prawo":
            prawo += 1
        if prev_move != "dol":
            dol += 1

        # zwracam najmniejsza mozliwosci
        return min(dol, prawo)

    res = ruch((0, 0))
    return None if res == inf else res


