<picture>
  <source srcset="../../srt/zbior_zadan/34.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_34.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_34.png" alt="zadanie 34">
</picture>

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