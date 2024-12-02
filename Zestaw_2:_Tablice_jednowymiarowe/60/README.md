<picture>
  <!-- Obraz dla ciemnego motywu -->
  <source srcset="../../srt/zbior_zadan/black_60.png" media="(prefers-color-scheme: dark)">
  <!-- Obraz dla jasnego motywu -->
  <source srcset="../../srt/zbior_zadan/black_60.png" media="(prefers-color-scheme: light)">
  <!-- Obraz domyślny (na wypadek braku wsparcia dla <picture>) -->
  <img src="../../srt/zbior_zadan/60.png" alt="Opis obrazu">
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
