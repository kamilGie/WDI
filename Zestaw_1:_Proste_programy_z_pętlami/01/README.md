![Zadanie 1](../../srt/zbior_zadan/01.png)

```python
def Zadanie_1(n):
    for a in range(1, n):
        for b in range(a, n):
            c = (a * a + b * b) ** 0.5
            if c.is_integer() and c < n:
                print(a, b, c)

```