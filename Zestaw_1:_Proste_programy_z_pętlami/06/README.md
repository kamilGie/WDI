<picture>
  <source srcset="../../srt/zbior_zadan/06.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_06.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_06.png" alt="zadanie 06">
</picture>


```python
def Zadanie_6(s):

    ε = 1e-6
    a1 = 1
    a2 = (s / a1 + a1) * 0.5

    while abs(a2 - a1) > ε:
        a1 = a2
        a2 = (s / a1 + a1) * 0.5

    return a2

```