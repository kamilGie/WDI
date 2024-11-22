# ====================================================================================================>
# Zadanie 165
# Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpo-
# wiada na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory
# o jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.
# ====================================================================================================>


def Zadanie_165(T, k): ...


if __name__ == "__main__":
    from testy165 import odpal_testy

    Zadanie_165(int(input('Podaj T: ')), int(input('Podaj k: ')))

    # odpal_testy()
