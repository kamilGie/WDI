# ====================================================================================================>
# Zadanie 2A, 16.12.2024
# Dwie liczby naturalne są 5-pokrewne, jeżeli po zapisaniu ich w systemie o podstawie 5,
# zbiory cyfr występujące w obu liczbach są identyczne. Na przykład:
# 21 = 41(5) i 34 = 114(5),
# 27 = 102(5) i 51 = 201(5).
#
# Dana jest szachownica o rozmiarze N x N, reprezentowana przez tablicę T wypełnioną liczbami naturalnymi.
# Sąsiedztwem danego pola na szachownicy są pola odległe o 1 lub 2 ruchy króla szachowego.
# Szczęśliwe pola to takie, które zawierają liczbę 5-pokrewną z liczbami na dokładnie 17 polach w swoim sąsiedztwie.
#
# Proszę napisać funkcję luck17(T), która sprawdza, czy w jakimkolwiek wierszu
# lub kolumnie znajduje się więcej niż jedno szczęśliwe pole.
#
# Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić wartość True albo False.
#
# Tablica reprezentująca szachownicę nie może ulec zmianie.
# ====================================================================================================>


def luck17(T): ...


if __name__ == "__main__":
    from testy2024_2A import odpal_testy

    luck17(int(input('Podaj T: ')))

    # odpal_testy()
