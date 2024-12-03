<picture>
  <source srcset="../../srt/zbior_zadan/65.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_65.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_65.png" alt="zadanie 65">
</picture>

```python
from random import randint


def is_odd_number(n):
    while n > 0:
        if (n % 10) % 2 == 1:
            return True
        else:
            n = n // 10

    return False


def list_check(tab):
    for el in tab:
        if not is_odd_number(el):
            return False

    return True


if __name__ == "__main__":
    n = int(input())
    tab = [randint(1, 1000) for _ in range(0, n)]

```