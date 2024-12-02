![Zadanie 21](../../srt/zbior_zadan/21.png)
```python
def golden_ratio(a, b):
    while abs((b / a) - (a + b) / b) > 0.00001:
        a, b = b, a + b

    return b / a



```