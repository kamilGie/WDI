<picture>
  <source srcset="../../srt/zbior_zadan/73.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_73.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_73.png" alt="zadanie 73">
</picture>

```python
def Zadanie_73(n):
    k = 365
    p_prim = 1
    for i in range(n):
        p_prim *= 1 - i / k

    return 1 - p_prim



```