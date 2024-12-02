<picture>
  <source srcset="../../srt/zbior_zadan/41.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_41.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_41.png" alt="zadanie 41">
</picture>

```python
from math import factorial


def Zadanie_41(N):
    silnia, d = divmod(factorial(N), 10)
    while d == 0:
        silnia, d = divmod(silnia, 10)

    return d



```