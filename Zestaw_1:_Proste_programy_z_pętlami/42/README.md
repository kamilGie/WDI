![Zadanie 42](../../srt/zbior_zadan/42.png)
```python
def policz_wystapienia_cyfry(liczba, cyfra):
    wystapienia = 0
    while liczba > 0:
        liczba, d = divmod(liczba, 10)
        if d == cyfra:
            wystapienia += 1
    return wystapienia


def Zadanie_42(a, b):
    for i in range(10):
        if policz_wystapienia_cyfry(a, i) != policz_wystapienia_cyfry(b, i):
            return False
    return True

```