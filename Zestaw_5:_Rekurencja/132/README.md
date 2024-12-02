<picture>
  <source srcset="../../srt/zbior_zadan/132.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_132.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_132.png" alt="zadanie 132">
</picture>

```python
def symbol_newtona(n, k):
    if k == 0 or k == n:
        return 1
    return symbol_newtona(n - 1, k - 1) + symbol_newtona(n - 1, k)


def Zadanie_132(n, k):
    if k * 2 > n:
        return symbol_newtona(n, n - k)
    return symbol_newtona(n, k)



```