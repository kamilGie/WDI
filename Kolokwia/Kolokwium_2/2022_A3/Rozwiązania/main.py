# ====================================================================================================>
# Zadanie A3, 20.12.2022
# Na szachownicy o wymiarach N × N umieszczono pewną liczbę pionków. Położenie pionków
# opisuje lista [(w0, k0),(w1, k1),(w2, k2), ...]. W lewym górnym rogu szachownicy (o współrzędnych 0, 0) znajduje się
# król, który musi dotrzeć do prawego dolnego rogu szachownicy. Król może wykonywać ruchy w prawo, w
# dół lub w górę szachownicy, nie może zbijać pionków ani wracać na pole, na którym już był. Proszę napisać
# funkcję king(N,L), która zwróci maksymalną liczbę ruchów jakie może wykonać król na drodze do celu. Do
# funkcji należy przekazać wyłącznie dwa parametry: rozmiar szachownicy N oraz listę L zawierającą położenia pionków. Jeżeli dotarcie do celu nie jest możliwe funkcja powinna zwrócić wartość None.
#  ====================================================================================================>

from math import inf


def king(N, L):
    # dodaje nie legalne ruchy czyli pozycje pionkow wraz z ich atakami
    forbidden = set()
    for px, py in L:
        forbidden.add((px, py))
        forbidden.add((px - 1, py - 1))
        forbidden.add((px - 1, py + 1))

    def maximize_moves(x, y, prev_move=None):
        """zwroci maxymalna ilosci ruchow do konca lub -inf jak sie nie da dotrzec do konca"""
        if not (0 <= x < N and 0 <= y < N) or (x, y) in forbidden:
            return -inf  # nie legalny ruch

        if (x, y) == (N - 1, N - 1):
            return 0  # Cel osiągnięty

        # krol moze porszuac sie tylko w prawo gore dol
        # zeby wrocim tam gdzie byl musial by po ruchu w gore
        # pojsc w dol nie ma innej opcji
        res = -inf
        if prev_move != "up":  # czy moge w dol
            res = max(res, maximize_moves(x + 1, y, "down"))
        if prev_move != "down":  # czy moge w gore
            res = max(res, maximize_moves(x - 1, y, "up"))
        res = max(res, (maximize_moves(x, y + 1)))  # W prawo

        # zwracam maxymalna liczbe ruchow najlepszego ruchu wraz z ruchem na pozycje tego ruchu
        return res + 1

    result = maximize_moves(0, 0)
    return None if result == -inf else result
