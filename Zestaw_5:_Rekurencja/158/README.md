<picture>
  <source srcset="../../srt/zbior_zadan/158.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_158.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_158.png" alt="zadanie 158">
</picture>

```python
def div(num):
    i = 2
    c_num = num
    arr = []
    while num > 1 and i < c_num:
        if num % i == 0:
            arr.append(i)
            while num % i == 0:
                num //= i
        i += 1

    return arr


def rek(t, index=0, jumps=0):
    if index >= len(t) - 1:
        if index == len(t) - 1:
            return jumps
        return -1

    divs = div(t[index])

    for divisor in divs:
        res = rek(t, index + divisor, jumps + 1)
        if res >= 0:
            return res

    return -1


def Zadanie_158(t):
    return rek(t)



```