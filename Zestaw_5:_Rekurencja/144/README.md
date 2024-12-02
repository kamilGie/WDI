![Zadanie 144](../../srt/zbior_zadan/144.png)
```python
def Zadanie_144(A, x):
    counter = rek(A, x)
    return counter


def rek(A, x, i=0, curr=1, dig_mult=0):
    if curr == x and i == len(A) and dig_mult > 1:
        return 1
    if curr > x or curr == 0 or i == len(A):
        return 0
    counter = 0
    counter += rek(A, x, i + 1, curr * A[i], dig_mult + 1)
    counter += rek(A, x, i + 1, curr, dig_mult)
    return counter

```