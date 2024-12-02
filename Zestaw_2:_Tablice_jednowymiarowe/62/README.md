![Zadanie 62](../../srt/zbior_zadan/62.png)
```python
from math import isqrt


def eratostenes(n):
    t = [True for _ in range(n + 1)]
    t[0] = t[1] = False

    for i in range(2, isqrt(n) + 1):
        if t[i]:
            for j in range(i * i, n + 1, i):
                t[j] = False

    for i in range(n):
        if t[i]:
            print(i, end=" ")



```