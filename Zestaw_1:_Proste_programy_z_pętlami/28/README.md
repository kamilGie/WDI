![Zadanie 28](../../srt/zbior_zadan/28.png)
```python
from math import isqrt


def Zadanie_28(n):
    i = isqrt(n)
    while i > 1:
        if n % i == 0:
            break
        i -= 1

    return i, n // i

```