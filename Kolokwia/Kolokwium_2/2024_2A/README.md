<picture>
  <source srcset="../../srt/zbior_zadan/2024_2A.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_2024_2A.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_2024_2A.png" alt="zadanie 2024_2A">
</picture>

```python
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
```

# Opis Rozwiązania

Tego seta można zastąpić tablicą 5-elementową lub liczbami w jakiejś dziwnej notacji.
Jednak w praktyce sprowadzi się to do tego samego. a set bedzie szybszy niz tablica

Podczas kolokwium, gdy ktoś zapytał, czy można tutaj użyć seta, Garek odpowiedział: 
"Można, ale jest to nieoptymalne. Niech się pan zastanowi, ile jest kombinacji tego zbioru."
Do tej pory nie rozumiem, o co chodziło w tej podpowiedzi. Gdy się dowiem, poprawię to.



