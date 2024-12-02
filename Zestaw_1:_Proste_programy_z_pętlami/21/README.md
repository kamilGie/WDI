<picture>
  <source srcset="../../srt/zbior_zadan/21.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_21.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_21.png" alt="zadanie 21">
</picture>

```python
def golden_ratio(a, b):
    while abs((b / a) - (a + b) / b) > 0.00001:
        a, b = b, a + b

    return b / a



```