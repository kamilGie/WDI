<picture>
  <source srcset="../../srt/zbior_zadan/29.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_29.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_29.png" alt="zadanie 29">
</picture>

```python
from math import isqrt


def czy_ciag(n):
    for i in range(1, isqrt(n) + 1):
        an = i * i + i + 1
        if n % an == 0:
            return True

    return False



```