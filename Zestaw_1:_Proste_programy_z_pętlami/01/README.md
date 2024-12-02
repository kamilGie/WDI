<picture>
  <source srcset="../../srt/zbior_zadan/01.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_01.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_01.png" alt="zadanie 01">
</picture>


```python
def Zadanie_1(n):
    for a in range(1, n):
        for b in range(a, n):
            c = (a * a + b * b) ** 0.5
            if c.is_integer() and c < n:
                print(a, b, c)

```