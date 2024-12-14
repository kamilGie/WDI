<picture>
  <source srcset="../../srt/zbior_zadan/117.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_117.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_117.png" alt="zadanie 117">
</picture>

```python

def czy_podciag_fibo(n1, n2, n3):
    """sprawdzi czy 3 elementy sa nastepnymi elemetami ciagu fibo"""
    a, b = 1, 0
    while n3 > a + b:
        a, b = a + b, a

    return n1 == b and n2 == a and n3 == a + b


def Podciag_fibo(s):
    """zwraca dlugosci podciagu fibo jesli jest dluzszy niz 2"""
    n = len(s)
    for i in range(n - 2):
        if czy_podciag_fibo(s[i], s[i + 1], s[i + 2]):
            res = 3
            for j in range(i + 1, n - 2):
                if s[j] + s[j + 1] != s[j + 2]:
                    break
                res += 1

            return res
    return 0


def Zadanie_117(T):
    n = len(T)

    # transpozycja T dla slicow kolumny
    transpozycja_T = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transpozycja_T[j][i] = T[i][j]

    for i in range(n):
        wiersz = Podciag_fibo(T[i])
        if wiersz > 2:
            return wiersz

        wiersz_odwrotnie = Podciag_fibo(T[i][::-1])
        if wiersz_odwrotnie > 2:
            return wiersz_odwrotnie

        kolumna = Podciag_fibo(transpozycja_T[i])
        if kolumna > 2:
            return kolumna

        kolumna_odwrotnie = Podciag_fibo(transpozycja_T[i][::-1])
        if kolumna_odwrotnie > 2:
            return kolumna_odwrotnie
```
# Opis Rozwiązania

Rozwiązanie zakłada, że w tablicy umieszczono *dokładnie jeden* fragment ciągu Fibonacciego.

Jest to imo najprostsze podejście, jakie można zastosować.

Możliwe jest jednak ulepszenie tego rozwiązania, na przykład poprzez dodanie dodatkowych warunków w funkcji `czy_podciag_fibo`.
- operacje typu `n3 > n1`
- [właściwości kwadratowe ciągu Fibonacciego](https://stackoverflow.com/questions/2432669/test-if-a-number-is-a-fibonacci-number):
```math
5n^2 + 4 \quad \text{lub} \quad 5n^2 - 4
```


---

Alternatywnie, można opracować bardziej optymalne podejście, które przekształca tablicę na indeksy ciągu Fibonacciego i sprawdza, czy któryś wiersz lub kolumna rośnie albo maleje.

###  Jednak takie rozwiązanie nie byłoby tak przejrzyste i proste jak obecne.
