![Zadanie 122](../../srt/zbior_zadan/122.png)
```python
def Zadanie_122(tab):
    for y in range(len(tab)):
        for x in range(y + 1, len(tab)):
            w1, k1 = tab[y]
            w2, k2 = tab[x]

            if w1 == w2 or k1 == k2:
                return False

            quotient = (w2 - w1) / (k2 - k1)
            if quotient == -1.00 or quotient == 1.00:
                return False

    return True



```