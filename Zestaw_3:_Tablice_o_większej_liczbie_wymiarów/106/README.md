<picture>
  <source srcset="../../srt/zbior_zadan/106.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_106.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_106.png" alt="zadanie 106">
</picture>

```python
def czy_zawiera(n):
    k = n
    primes = {2, 3, 5, 7}

    while k > 0:
        if (k % 10) in primes:
            return True
        k = k // 10
    # end while
    return False


def Zadanie_106(tab):
    n = len(tab)

    for y in range(n):
        flag = True
        for x in range(n):
            if not czy_zawiera(tab[y][x]):
                flag = False
                break
        # end for 2
        if flag:
            return True
        flag = True
    # end for 1
    return False



```