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


def rook(N, L): ...


if __name__ == "__main__":
    from testy2022_B3 import odpal_testy

    rook(5, [(1, 2), (0, 2), (2, 0), (3, 3)])  # return  3

    # odpal_testy()
