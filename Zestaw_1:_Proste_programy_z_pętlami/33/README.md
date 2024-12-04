<picture>
  <source srcset="../../srt/zbior_zadan/33.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_33.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_33.png" alt="zadanie 33">
</picture>

```python
def Zadanie_33(n):
    if n < 10:
        return True

    ostatnia, n = n % 10, n // 10
    przedostatnia = n % 10
    if ostatnia == 0 or przedostatnia == 0:
        return False

    r = ostatnia / przedostatnia
    while n >= 10:
        ostatnia, n = przedostatnia, n // 10
        przedostatnia = n % 10
        if ostatnia == 0 or przedostatnia == 0 or ostatnia / przedostatnia != r:
            return False

    return True



```