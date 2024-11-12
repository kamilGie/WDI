# ====================================================================================================>
# Zadanie 111
# Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
# przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
# wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
# ====================================================================================================>

# jak bede mial czas wymysle testy


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
    kolumny, wiersze = sum_of_table(
        tab
    )  # tablice z sumami poszczególnych wierszy i kolumn
    suma = 0
    best = 0

    for y in range(n - 1):  # y i x to wspolrzedne pierwszej wieży
        for x in range(n - 1):
            for a in range(y + 1, n):  # a i b to wspolrzedne drugiej wiezy
                for b in range(
                    x + 1, n
                ):  # można dać range(n), ale wolniej to jest wtedy
                    if b != x:
                        suma = (
                            wiersze[y]
                            + kolumny[x]
                            + wiersze[a]
                            + kolumny[b]
                            - tab[y][b]
                            - tab[a][x]
                        )
                        suma = suma - 2 * tab[y][x] - 2 * tab[a][b]
                    if suma > best:
                        best = suma
                        crd = ([y, x], [a, b])

    return best, crd


if __name__ == "__main__":
    from Develop import stworz_zadanie

    stworz_zadanie([Zadanie_111])
