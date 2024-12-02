<picture>
  <source srcset="../../srt/zbior_zadan/104.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_104.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_104.png" alt="zadanie 104">
</picture>

```python
from math import sqrt


def czy_pierwsza(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i < sqrt(n) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    # end
    return True


def Zadanie_104(tab):
    n = len(tab)
    for y in range(n):
        for x in range(n):
            for i in range(n):
                found = False
                for j in range(n):
                    if y == i and x == j:
                        continue
                    if tab[i][j] == 0:
                        continue
                    if czy_pierwsza(tab[y][x] + tab[i][j]):
                        found = True
                        break
                # end for j
                if found:
                    break

            # end for i
            else:
                tab[y][x] = 0
        # end for x
    # end for y
    return tab



```