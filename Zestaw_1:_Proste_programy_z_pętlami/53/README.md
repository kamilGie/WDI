<picture>
  <source srcset="../../srt/zbior_zadan/53.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_53.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_53.png" alt="zadanie 53">
</picture>

```python
def is_two_three_five(num):
    for div in {2, 3, 5}:
        while num % div == 0:
            num //= div
    return num == 1


def Zadanie_53(n):
    counter = 0
    for i in range(1, n + 1):
        if is_two_three_five(i):
            counter += 1

    return counter



```