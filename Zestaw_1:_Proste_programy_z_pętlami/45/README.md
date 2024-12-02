![Zadanie 45](../../srt/zbior_zadan/45.png)
```python
from math import sqrt


def Zadanie_45(m, n):

    rozwiniecie = int(sqrt(m) * 10**n)

    suma = 0
    for _ in range(n):
        rozwiniecie, d = divmod(rozwiniecie, 10)
        suma += d
    return suma



```