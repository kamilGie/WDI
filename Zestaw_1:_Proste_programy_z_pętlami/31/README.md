![Zadanie 31](../../srt/zbior_zadan/31.png)
```python
def czy_ciag(n):
    an = 2
    while an <= n:
        if n % an == 0:
            return True
        an = 3 * an + 1

    return False



```