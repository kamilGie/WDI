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


def cyfry_piatkowe(x):
    """Zwraca zbiór cyfr liczby x w systemie o podstawie 5."""
    res = set()
    while x > 0:
        x, d = divmod(x, 5)
        res.add(d)
    return res


def sasiadujace_pola(i, j, n):
    """generuje sąsiednie pola odległe o 1 lub 2 ruchy króla szachowego."""
    for dx in range(-2, 3):  # Ruchy w zakresie -2, 2
        for dy in range(-2, 3):
            if dx == 0 and dy == 0:  # Pomijamy samo pole
                continue
            if 0 <= i + dx < n and 0 <= j + dy < n:  # czy pole jest w granicach
                yield (i + dx, j + dy)


def czy_szczesliwe(i, j, T):
    liczba_pokrewnych = 0
    cyfry_srodkowe = cyfry_piatkowe(T[i][j])

    for x, y in sasiadujace_pola(i, j, len(T)):
        if cyfry_piatkowe(T[x][y]) == cyfry_srodkowe:
            liczba_pokrewnych += 1

    return liczba_pokrewnych == 17


def luck17(T):
    n = len(T)
    szczesliwe_wiersze = [0] * n
    szczesliwe_kolumny = [0] * n

    # Sprawdzamy każde pole szachownicy
    for i in range(1, n - 1):  # bez granic bo one nie moga miec 17 sasiadow
        for j in range(1, n - 1):
            if czy_szczesliwe(i, j, T):
                szczesliwe_wiersze[i] += 1
                szczesliwe_kolumny[j] += 1

                # Jeśli już więcej niż jedno szczęśliwe pole w wierszu lub kolumnie
                if szczesliwe_wiersze[i] > 1 or szczesliwe_kolumny[j] > 1:
                    return True
    return False


