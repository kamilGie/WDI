![Zadanie 16](../../srt/zbior_zadan/16.png)
```python
def NWD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def NWW(a, b):
    return (a * b) // (NWD(a, b))


def NWW_3(a, b, c):
    return NWW(NWW(a, b), c)



```