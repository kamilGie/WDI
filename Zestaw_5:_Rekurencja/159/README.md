<picture>
  <source srcset="../../srt/zbior_zadan/159.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_159.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_159.png" alt="zadanie 159">
</picture>

```python
from math import sqrt


def prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i <= sqrt(n) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    # end while
    return True


def Zadanie_159(A, B):
    num = 2 ** (A + B - 1)
    suma = 0

    def rek(A, B, num):
        nonlocal suma
        if A == 0 and B == 0:
            if not prime(num):
                suma += 1
                print(num)

            return
        # end if

        if A > 0:
            rek(A - 1, B, num + 2 ** (A + B - 1))
        if B > 0:
            rek(A, B - 1, num)

    # end def 2
    rek(A - 1, B, num)
    return suma

```