![Zadanie 70](../../srt/zbior_zadan/70.png)
```python
def longest_geometric_series(tab: list):
    if len(tab) < 2:
        return len(tab)
    counter = 2
    best_length = 2

    q = round(tab[1] / tab[0], 5)

    for i in range(2, len(tab)):
        if round(tab[i] / tab[i - 1], 5) == q:
            counter += 1
        else:
            best_length = max(best_length, counter)
            counter = 2
            q = round(tab[i] / tab[i - 1], 5)
        # end if
    # end for
    return max(best_length, counter)



```