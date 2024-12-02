![Zadanie 73](../../srt/zbior_zadan/73.png)
```python
def Zadanie_73(n):
    k = 365
    p_prim = 1
    for i in range(n):
        p_prim *= 1 - i / k

    return 1 - p_prim



```