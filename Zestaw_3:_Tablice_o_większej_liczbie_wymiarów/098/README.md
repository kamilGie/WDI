![Zadanie 098](../../srt/zbior_zadan/098.png)
```python
def Zadanie_98(T1, T2):
    indeks_T2 = 0  # Początkowy indeks dla T2
    for tab in T1:
        for element in tab:
            k = indeks_T2 - 1
            while k >= 0 and T2[k] > element:
                T2[k + 1] = T2[k]
                k -= 1
            T2[k + 1] = element
            indeks_T2 += 1

    return T2



```