# ====================================================================================================>
# Zadanie 154
# Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool.
# ====================================================================================================>


def Zadanie_154(T, k): ...


if __name__ == "__main__":
    from testy154 import odpal_testy

    Zadanie_154(int(input('Podaj T: ')), int(input('Podaj k: ')))

    # odpal_testy()
