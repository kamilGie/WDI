<picture>
  <source srcset="../../srt/zbior_zadan/17.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_17.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_17.png" alt="zadanie 17">
</picture>

```python
# z bit ale nie wiem jak to ma niby dzialac xdd

from math import pi

# https://pl.wikipedia.org/wiki/Wzór_Taylora


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def cos(x, n):
    result = 0
    for i in range(n + 1):
        result += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    return result


print(cos(pi / 2, 30))



```