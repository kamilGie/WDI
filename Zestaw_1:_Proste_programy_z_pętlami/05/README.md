<picture>
  <source srcset="../../srt/zbior_zadan/05.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_05.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_05.png" alt="zadanie 05">
</picture>

```python
def Zadanie_5(liczba: int):
    suma = 0
    licznik = 0
    nieparzysta = 1

    while suma <= liczba:
        suma += nieparzysta
        nieparzysta += 2
        licznik += 1

    return licznik - 1



```