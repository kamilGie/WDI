<picture>
  <source srcset="../../srt/zbior_zadan/2024_2B.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_2024_2B.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_2024_2B.png" alt="zadanie 2024_2B">
</picture>

```python
from math import isqrt


def isprime(x):
    """sprawdza czy liczby wieksze od 1 sa pierwsze"""
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, isqrt(x) + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True


def a(x):
    res = 0
    while x > 0:
        x, d = divmod(x, 10)
        res = res * 10 + d
    return res + 1


def b(x):
    while True:
        x += 1
        if isprime(x):
            return x


def c(x):
    res = 1 / x
    while int(res) == 0:  # usuwanie zer z przodu
        res *= 10
    return int(res * 100)  # 3 cyfry rozwiniecia


def cykl(x):
    def rek(l, i):
        if i == 10:  #  za dlugi
            return ""
        if l == x and i > 0:  # sukces
            return ""

        na = "A" + rek(a(l), i + 1)
        nb = "B" + rek(b(l), i + 1)
        nc = "C" + rek(c(l), i + 1)
        return min(na, nb, nc, key=len)  # najmniejszy napis

    res = rek(x, 0)
    return ( res if len(res) < 10 else "")  # jesli napis jest krotszy niz 10 to znaleziono taki cykl
```