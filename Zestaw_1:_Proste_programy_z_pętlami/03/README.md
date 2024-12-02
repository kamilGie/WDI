<picture>
  <source srcset="../../srt/zbior_zadan/03.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_03.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_03.png" alt="zadanie 03">
</picture>

```python
def Zadanie_3():
    rok = 2024
    best = (rok - 1, 1)

    for i in range(1, rok + 1):
        x = i
        y = rok
        while y > x:
            x, y = y - x, x
        if x + y < sum(best):
            best = (x, y)
    print(best)


if __name__ == "__main__":

    Zadanie_3()

```