![Zadanie 132](../../srt/zbior_zadan/132.png)
```python
def symbol_newtona(n, k):
    if k == 0 or k == n:
        return 1
    return symbol_newtona(n - 1, k - 1) + symbol_newtona(n - 1, k)


def Zadanie_132(n, k):
    if k * 2 > n:
        return symbol_newtona(n, n - k)
    return symbol_newtona(n, k)



```