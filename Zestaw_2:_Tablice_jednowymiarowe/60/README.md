![Zadanie 60](../../srt/zbior_zadan/60.png)
```python
def zamien_na_system(liczba, podstawa):
    znaki = "0123456789ABCDEF"
    wynik = ""

    while liczba > 0:
        reszta = liczba % podstawa
        wynik = znaki[reszta] + wynik
        liczba //= podstawa

    return wynik or "0"


def Zadanie_60(liczba):
    for i in range(2, 17):
        print(zamien_na_system(liczba, i), end=" ")



```