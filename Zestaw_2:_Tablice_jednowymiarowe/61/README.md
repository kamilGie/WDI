<picture>
  <source srcset="../../srt/zbior_zadan/61.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_61.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_61.png" alt="zadanie 61">
</picture>

```python
def same_digits(a, b):
    tab = [0 for _ in range(0, 10)]

    while a > 0:
        tab[a % 10] += 1
        a = a // 10
    # end while

    while b > 0:
        tab[b % 10] -= 1
        b = b // 10
    # end while

    for element in tab:
        if element != 0:
            return False
    # end for
    return True


# --- main



```