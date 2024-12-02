<picture>
  <source srcset="../../srt/zbior_zadan/28.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_28.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_28.png" alt="zadanie 28">
</picture>

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