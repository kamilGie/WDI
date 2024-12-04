<picture>
  <source srcset="../../srt/zbior_zadan/31.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_31.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_31.png" alt="zadanie 31">
</picture>

```python
def czy_ciag(n):
    an = 2
    while an <= n:
        if n % an == 0:
            return True
        an = 3 * an + 1

    return False



```