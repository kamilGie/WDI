![Zadanie 41](../../srt/zbior_zadan/41.png)
```python
from math import factorial


def Zadanie_41(N):
    silnia, d = divmod(factorial(N), 10)
    while d == 0:
        silnia, d = divmod(silnia, 10)

    return d



```