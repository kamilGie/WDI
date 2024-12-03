<picture>
  <source srcset="../../srt/zbior_zadan/09.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_09.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_09.png" alt="zadanie 09">
</picture>

```python
def iloczyn(liczba):
    a, b = 1, 1
    while a * b < liczba:
        a, b = b, a + b

    return a * b == liczba



```