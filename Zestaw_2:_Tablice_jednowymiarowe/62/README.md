<picture>
  <source srcset="../../srt/zbior_zadan/62.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_62.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_62.png" alt="zadanie 62">
</picture>

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