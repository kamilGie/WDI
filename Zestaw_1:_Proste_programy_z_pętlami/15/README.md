![Zadanie 15](../../srt/zbior_zadan/15.png)
```python
def nwd(a, b):
    while b != 0:
        b, a = a % b, b
    return a


def nwd3(a, b, c):
    return nwd(nwd(a, b), c)



```