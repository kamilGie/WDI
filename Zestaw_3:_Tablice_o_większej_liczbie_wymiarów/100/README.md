![Zadanie 100](../../srt/zbior_zadan/100.png)
```python
def Zadanie_100(T, k):
    n = len(T)

    for y in range(n):
        for x in range(n):
            bok = 2
            iloczyn = 1
            while y + bok < n and x + bok < n:
                iloczyn = T[y][x] * T[y + bok][x] * T[y][x + bok] * T[y + bok][x + bok]

                if iloczyn == k:
                    return (y + y + bok) // 2, (x + x + bok) // 2
                bok += 2
    return False



```