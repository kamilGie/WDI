<picture>
  <source srcset="../../srt/zbior_zadan/30.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_30.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_30.png" alt="zadanie 30">
</picture>

```python
def pole(k):
    eps = 0.0001
    x = 1
    suma = 0

    while x < k:
        suma += (1 / x) * eps
        x += eps

    return suma



```