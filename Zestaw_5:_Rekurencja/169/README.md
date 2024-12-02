![Zadanie 169](../../srt/zbior_zadan/169.png)
```python
def czy_wspolno_czynikowe(a, b):
    """
    Dwie liczby są wspólno-czynnikowe, jeśli ich NWD jest liczbą pierwszą.
    """

    def nwd(x, y):
        while y:
            x, y = y, x % y
        return x

    def czy_pierwsza(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    return czy_pierwsza(nwd(a, b))


def four(T):
    licznik = 0
    directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
    N = len(T)

    # Iterujemy tylko po wnętrzu tablicy (bez krawędzi)
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            wspolno_czynnikowe = 0

            # Sprawdzamy wszystkich sąsiadów
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if czy_wspolno_czynikowe(T[i][j], T[x][y]):
                    wspolno_czynnikowe += 1

            # Jeżeli liczba ma dokładnie 4 sąsiadów wspólno-czynnikowych, zwiększamy licznik
            if wspolno_czynnikowe == 4:
                licznik += 1

    return licznik

```