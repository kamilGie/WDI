![Zadanie 39](../../srt/zbior_zadan/39.png)
```python
from math import factorial


def Zadanie_39(N):
    liczba_zer = 0

    silnia, d = divmod(factorial(N), 10)
    while d == 0:
        liczba_zer += 1
        silnia, d = divmod(silnia, 10)

    return liczba_zer



```