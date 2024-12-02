![Zadanie 35](../../srt/zbior_zadan/35.png)
```python
def Zadanie_35(n):
    n, uniklana_cyfra = divmod(n, 10)
    while n > 0:
        n, liczba = divmod(n, 10)
        if liczba == uniklana_cyfra:
            return False
    return True



```