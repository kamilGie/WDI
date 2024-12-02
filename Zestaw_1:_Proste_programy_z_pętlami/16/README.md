<picture>
  <source srcset="../../srt/zbior_zadan/16.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_16.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_16.png" alt="zadanie 16">
</picture>

```python
def NWD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def NWW(a, b):
    return (a * b) // (NWD(a, b))


def NWW_3(a, b, c):
    return NWW(NWW(a, b), c)



```