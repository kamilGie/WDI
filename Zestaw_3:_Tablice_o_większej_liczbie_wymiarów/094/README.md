<picture>
  <source srcset="../../srt/zbior_zadan/094.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_094.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_094.png" alt="zadanie 094">
</picture>

```python
def at_least_one_even(n):
    temp = n
    while temp != 0:
        if (temp % 10) % 2 == 0:
            return True
        temp = temp // 10
    # end while
    return False


def even_in_verse(tab):
    for element in tab:
        if not at_least_one_even(element):
            return False
    # end for
    return True


def check_tab_for_even_verses(tab):
    for i in tab:
        if even_in_verse(i):
            return True
    # end for
    return False



```