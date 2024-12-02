![Zadanie 09](../../srt/zbior_zadan/09.png)
```python
def iloczyn(liczba):
    a, b = 1, 1
    while a * b < liczba:
        a, b = b, a + b

    return a * b == liczba



```