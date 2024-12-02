![Zadanie 66](../../srt/zbior_zadan/66.png)
```python
from random import randint


def is_all_odd_number(n):
    while n > 0:
        if (n % 10) % 2 == 0:
            return False
        else:
            n = n // 10

    return True


def list_check(tab):
    for el in tab:
        if is_all_odd_number(el):
            return True

    return False


if __name__ == "__main__":

    n = int(input())
    tab = [randint(1, 1000) for _ in range(0, n)]
    list_check(tab)


```