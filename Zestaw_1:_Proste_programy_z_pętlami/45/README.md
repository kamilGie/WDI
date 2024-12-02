<picture>
  <source srcset="../../srt/zbior_zadan/45.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_45.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_45.png" alt="zadanie 45">
</picture>

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