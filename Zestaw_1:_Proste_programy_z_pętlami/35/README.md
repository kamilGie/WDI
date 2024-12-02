<picture>
  <source srcset="../../srt/zbior_zadan/35.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_35.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_35.png" alt="zadanie 35">
</picture>

```python
def Zadanie_35(n):
    n, uniklana_cyfra = divmod(n, 10)
    while n > 0:
        n, liczba = divmod(n, 10)
        if liczba == uniklana_cyfra:
            return False
    return True



```