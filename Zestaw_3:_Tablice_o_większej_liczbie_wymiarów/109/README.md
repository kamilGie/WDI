<picture>
  <source srcset="../../srt/zbior_zadan/109.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_109.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_109.png" alt="zadanie 109">
</picture>

```python
def Zadanie_109(tab):
    n = len(tab)
    res = suma = 0

    for y in range(n):
        for x in range(n):
            for i in range(1, 11):

                if i + y < n:
                    suma = 0
                    for j in range(y, i + y + 1):
                        suma += tab[j][x]
                    res = max(res, suma)

                if i + x < n:
                    suma = 0
                    for j in range(x, i + x + 1):
                        suma += tab[y][j]
                    res = max(res, suma)
    return res



```