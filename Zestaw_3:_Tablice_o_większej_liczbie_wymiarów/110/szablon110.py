# ====================================================================================================>
# Zadanie 110
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
# szachowego.
# ====================================================================================================>


def Zadanie_110(T, k): ...


if __name__ == "__main__":
    from testy110 import odpal_testy

    Zadanie_110(int(input('Podaj T: ')), int(input('Podaj k: ')))

    # odpal_testy()
