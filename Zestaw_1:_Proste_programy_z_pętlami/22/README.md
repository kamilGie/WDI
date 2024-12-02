![Zadanie 22](../../srt/zbior_zadan/22.png)
```python
def Zadanie_22():
    e = 0
    n = 0
    silnia = 1
    wzrost = 1
    while wzrost > 1e-6:
        wzrost = 1 / silnia
        e += wzrost
        n += 1
        silnia = silnia * n
    return e

```