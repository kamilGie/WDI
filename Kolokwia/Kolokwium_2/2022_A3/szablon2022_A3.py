# ====================================================================================================>
# Zadanie A3, 20.12.2022
# Na szachownicy o wymiarach N × N umieszczono pewną liczbę pionków. Położenie pionków
# opisuje lista [(w0, k0),(w1, k1),(w2, k2), ...]. W lewym górnym rogu szachownicy (o współrzędnych 0, 0) znajduje się
# król, który musi dotrzeć do prawego dolnego rogu szachownicy. Król może wykonywać ruchy w prawo, w
# dół lub w górę szachownicy, nie może zbijać pionków ani wracać na pole, na którym już był. Proszę napisać
# funkcję king(N,L), która zwróci maksymalną liczbę ruchów jakie może wykonać król na drodze do celu. Do
# funkcji należy przekazać wyłącznie dwa parametry: rozmiar szachownicy N oraz listę L zawierającą położenia pionków. Jeżeli dotarcie do celu nie jest możliwe funkcja powinna zwrócić wartość None.
#  ====================================================================================================>


def king(N, L): ...


if __name__ == "__main__":
    from testy2022_A3 import odpal_testy

    king(int(input("Podaj N: ")), list(input("Podaj L: ")))

    # odpal_testy()
