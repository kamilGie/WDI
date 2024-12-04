<picture>
  <source srcset="../../srt/zbior_zadan/18.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_18.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_18.png" alt="zadanie 18">
</picture>

```python
from math import sqrt


def Zadanie_18():

    a1 = sqrt(0.5)
    a2 = sqrt(0.5 + 0.5 * a1)
    iloczyn = a1 * a2

    while abs(a2 - a1) > 0.00000001:
        a1 = a2
        a2 = sqrt(0.5 + 0.5 * a1)
        iloczyn *= a2

    print(2 / iloczyn)



```