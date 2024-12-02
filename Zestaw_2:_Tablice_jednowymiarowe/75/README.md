![Zadanie 75](../../srt/zbior_zadan/75.png)
```python
def Zadanie_75(T):
    if len(T) < 1:
        return False

    min = max = T[0]
    min_jedyny = max_jedyny = True

    for el in T[1:]:
        if min > el:
            min = el
            min_jedyny = True
        elif min == el:
            min_jedyny = False

        if max < el:
            max = el
            max_jedyny = True
        elif max == el:
            max_jedyny = False

    return min_jedyny and max_jedyny



```