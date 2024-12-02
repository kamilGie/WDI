<picture>
  <source srcset="../../srt/zbior_zadan/38.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_38.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_38.png" alt="zadanie 38">
</picture>

```python
def Zadanie_38():
    a1, a2, a3, a4, a5 = (int(input()) for _ in range(1, 6))

    while a5 != 0:
        if (a1 + a2 + a4 + a5) / 4 == a3:
            print(f"srednia:{a3}")
        a1, a2, a3, a4, a5 = a2, a3, a4, a5, int(input())

```