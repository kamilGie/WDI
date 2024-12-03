<picture>
  <source srcset="../../srt/zbior_zadan/15.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_15.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_15.png" alt="zadanie 15">
</picture>

```python
def nwd(a, b):
    while b != 0:
        b, a = a % b, b
    return a


def nwd3(a, b, c):
    return nwd(nwd(a, b), c)



```