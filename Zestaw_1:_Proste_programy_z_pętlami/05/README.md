![Zadanie 05](../../srt/zbior_zadan/05)
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