![Zadanie 38](../../srt/zbior_zadan/38.png)
```python
def Zadanie_38():
    a1, a2, a3, a4, a5 = (int(input()) for _ in range(1, 6))

    while a5 != 0:
        if (a1 + a2 + a4 + a5) / 4 == a3:
            print(f"srednia:{a3}")
        a1, a2, a3, a4, a5 = a2, a3, a4, a5, int(input())

```