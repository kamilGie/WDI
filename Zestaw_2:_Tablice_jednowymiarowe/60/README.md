<picture>
  <source srcset="../../srt/zbior_zadan/60.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_60.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_60.png" alt="zadanie 60">
</picture>

  <source srcset="../../srt/zbior_zadan/60.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_60.png" media="(prefers-color-scheme: dark)">
  <img src="./srt/zbior_zadan/black_60.png" alt="zdjecie z plocka">
</picture>

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
