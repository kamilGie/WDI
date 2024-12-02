![Zadanie 29](../../srt/zbior_zadan/29.png)
```python
from math import isqrt


def czy_ciag(n):
    for i in range(1, isqrt(n) + 1):
        an = i * i + i + 1
        if n % an == 0:
            return True

    return False



```