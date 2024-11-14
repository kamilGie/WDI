# ====================================================================================================>
# Zadanie 111
# Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
# przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
# wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
# ====================================================================================================>
# return tuple(wiersz1,kolumna1, wiersz2,kolumna2)

# z wiki bledne bo liczy pola  dwurkotnie gdy wieze sa w tym samym wierzu/kolumnie


def sum_of_table(tab):
    n = len(tab)
    kolumny = [0] * n
    wiersze = [0] * n
    suma = 0

    for y in range(n):
        for x in range(n):
            suma += tab[y][x]
        wiersze[y] = suma
        suma = 0

    for x in range(n):
        for y in range(n):
            suma += tab[y][x]
        kolumny[x] = suma
        suma = 0

    return kolumny, wiersze


def Zadanie_111(tab):
    n = len(tab)
    kolumny, wiersze = sum_of_table(tab)
    suma = 0
    best = float("-inf")
    best_positions = None

    for y in range(n):
        for x in range(n):
            for a in range(y + 1, n):
                for b in range(x + 1, n):
                    suma = (
                        wiersze[y]
                        + kolumny[x]
                        + wiersze[a]
                        + kolumny[b]
                        - tab[y][x]  # Pole, na którym stoi pierwsza wieża
                        - tab[a][b]  # Pole, na którym stoi druga wieża
                    )

                    if y == a and x == b:
                        suma -= tab[y][x]

                    if suma > best:
                        best = suma
                        best_positions = ([y, x], [a, b])

    return best_positions


if __name__ == "__main__":
    from Develop import stworz_zadanie

    stworz_zadanie([Zadanie_111])
