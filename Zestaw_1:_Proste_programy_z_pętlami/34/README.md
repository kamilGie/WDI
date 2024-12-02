![Zadanie 34](../../srt/zbior_zadan/34.png)
```python
import math


def Zadanie_34(n):
    liczba_cyfr = math.floor(math.log10(n)) + 1

    if liczba_cyfr > 9:
        return False

    while n > 0:
        n, d = divmod(n, 10)
        if d == liczba_cyfr:
            return True

    return False



```