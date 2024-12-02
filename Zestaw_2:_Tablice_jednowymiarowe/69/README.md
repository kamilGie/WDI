<picture>
  <source srcset="../../srt/zbior_zadan/69.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_69.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_69.png" alt="zadanie 69">
</picture>

```python
def longest_increasing_series(tab):
    counter = 1
    best_length = 1
    for i in range(1, len(tab)):
        if tab[i] > tab[i - 1]:
            counter += 1
        else:
            best_length = max(best_length, counter)
            counter = 1
        # end if
    # end for
    return max(best_length, counter)



```