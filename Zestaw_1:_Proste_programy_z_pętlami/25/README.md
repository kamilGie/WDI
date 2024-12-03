<picture>
  <source srcset="../../srt/zbior_zadan/25.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_25.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_25.png" alt="zadanie 25">
</picture>

```python
from math import sqrt


def Zadanie_25(n):
    a1, a2 = 1, 1

    while a1 < sqrt(n) + 1:
        if n % a1 == 0:
            b1, b2 = a1, a2

            while a1 * b1 < n:
                b1, b2 = b2, b1 + b2

            if a1 * b1 == n:
                return True

        a1, a2 = a2, a1 + a2

    return False



```