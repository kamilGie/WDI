![Zadanie 30](../../srt/zbior_zadan/30.png)
```python
def pole(k):
    eps = 0.0001
    x = 1
    suma = 0

    while x < k:
        suma += (1 / x) * eps
        x += eps

    return suma



```