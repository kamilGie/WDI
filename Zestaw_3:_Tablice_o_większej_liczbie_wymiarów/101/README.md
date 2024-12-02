<picture>
  <source srcset="../../srt/zbior_zadan/101.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_101.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_101.png" alt="zadanie 101">
</picture>

```python
def Zadanie_101(tab):
    n = len(tab)
    column = [0 for i in range(n)]

    for y in range(n):
        flag = False
        for x in range(n):
            if tab[y][x] == 0:
                flag = True
                column[x] = 1
            # end if
        # end for 2
        if not flag:
            return False
        else:
            flag = True
    # end for 1

    for element in column:
        if element == 0:
            return False
    # end for
    return True



```