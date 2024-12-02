<picture>
  <source srcset="../../srt/zbior_zadan/133.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_133.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_133.png" alt="zadanie 133">
</picture>

```python
from math import log10, floor, sqrt


def prime_dwucyfrowy(n):
    if n < 10 or n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i <= sqrt(n) + 1:
        if n % i == 0:
            return False
        else:
            i += 2
            if n % i == 0:
                return False
            i += 4
    # end while
    return True


def Zadanie_133(x):
    N = floor(log10(x)) + 1

    def rek(x, y, i):
        if x == 0:
            if i != N and i >= 2 and prime_dwucyfrowy(y):
                print(y)
        else:
            rek(x // 10, y, i)
            rek(x // 10, y + (x % 10) * (10**i), i + 1)

    rek(x, 0, 0)



```