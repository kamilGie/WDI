![Zadanie 126](../../srt/zbior_zadan/126.png)
```python
def dodawanie(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]


def odejmowanie(c1, c2):
    return c1[0] - c2[0], c1[1] - c2[1]


def mnozenie(c1, c2):
    return c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c1[1] * c2[0]


def dzielenie(c1, c2):
    re2, im2 = c2
    sprzegenie_c2 = (re2, -im2)
    licznik = mnozenie(c1, sprzegenie_c2)
    mianownik = re2**2 + im2**2
    re, im = licznik
    return re / mianownik, im / mianownik


def potegowanie(c1, n):
    re, im = c1
    wynik_re = 1
    wynik_im = 0
    for _ in range(n):
        wynik_re, wynik_im = mnozenie((wynik_re, wynik_im), (re, im))
    return wynik_re, wynik_im


import cmath


def pierwiastek(c1):
    z = complex(c1[0], c1[1])
    pierwiastek_z = cmath.sqrt(z)
    pierwiastek1 = (pierwiastek_z.real, pierwiastek_z.imag)
    return pierwiastek1


def Zadanie_126(a, b, c):
    delta = odejmowanie(potegowanie(b, 2), mnozenie((4, 0), mnozenie(a, c)))
    sqrt_delta1 = pierwiastek(delta)
    print(sqrt_delta1)
    denominator = mnozenie((2, 0), a)
    minus_b = mnozenie((-1, 0), b)

    licznik = odejmowanie(minus_b, sqrt_delta1)
    z1_re, z1_im = dzielenie(licznik, denominator)
    licznik = dodawanie(minus_b, sqrt_delta1)
    z2_re, z2_im = dzielenie(licznik, denominator)

    return (z1_re, z1_im), (z2_re, z2_im)



```