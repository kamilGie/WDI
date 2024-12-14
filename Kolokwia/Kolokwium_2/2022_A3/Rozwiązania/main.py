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


def maximize_moves(x, y, forbidden, N, prev_move=None):
    """Zwroci maxymalna ilosci ruchow do konca lub -inf jak sie nie da dotrzec do konca"""
    # Sprawdzam czy jestem na legalnej pozycji
    if (x, y) in forbidden:  # Zajęte
        return -inf
    if not (0 <= x < N and 0 <= y < N):  # za granicami szachownicy
        return -inf

    if (x, y) == (N - 1, N - 1):
        return 0  # Cel osiągnięty

    res = -inf
    # Zeby krol wrocim tam gdzie byl musialby po ruchu w gore pojsc w dol lub na odwrot
    if prev_move != "up":  # czy moge w dol
        res = max(res, maximize_moves(x + 1, y, forbidden, N, "down") + 1)
    if prev_move != "down":  # czy moge w gore
        res = max(res, maximize_moves(x - 1, y, forbidden, N, "up") + 1)
    res = max(res, (maximize_moves(x, y + 1, forbidden, N)) + 1)  # W prawo

    # Zwracam maxymalna liczbe ruchow najlepszego ruchu
    return res


def king(N, L):
    result = maximize_moves(0, 0, L, N)
    return None if result == -inf else result
