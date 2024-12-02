![Zadanie 32](../../srt/zbior_zadan/32.png)
```python
def Zadanie_32(n):
    ostatnie_d = 10
    while n > 0:
        n, d = divmod(n, 10)
        if ostatnie_d <= d:
            return False
        ostatnie_d = d
    return True



```