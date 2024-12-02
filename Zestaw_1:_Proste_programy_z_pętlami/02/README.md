<picture>
  <source srcset="../../srt/zbior_zadan/02.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_02.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_02.png" alt="zadanie 02">
</picture>

```python
def Zadanie_2():
    a = b = 1
    while a < 1e6:
        print(a, end=" ")
        a, b = b, a + b

```