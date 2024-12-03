<picture>
  <source srcset="../../srt/zbior_zadan/70.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_70.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_70.png" alt="zadanie 70">
</picture>

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