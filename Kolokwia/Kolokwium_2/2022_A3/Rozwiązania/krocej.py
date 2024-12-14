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
    def maximize_moves(x, y, prev_move=None):
        if not (0 <= x < N and 0 <= y < N) or (x, y) in L:
            return -inf # nie legalny ruch

        if (x, y) == (N - 1, N - 1): # meta
            return 0

        res = -inf
        if prev_move != "up":  # czy moge w dol
            res = maximize_moves(x + 1, y, "down")
        if prev_move != "down":  # czy moge w gore
            res = max(res, maximize_moves(x - 1, y, "up"))
        return max(res, (maximize_moves(x, y + 1))) + 1  # W prawo

    result = maximize_moves(0, 0)
    return None if result == -inf else result

