![Zadanie 55](../../srt/zbior_zadan/55.png)
```python
# rozwiazanie z wiki ale posiada tablice


def common_digit(a, b, s):
    tab = [False for _ in range(s)]

    while a != 0:
        tab[a % s] = True
        a = a // s
    # end while

    while b != 0:
        if tab[b % s]:
            return False
        b = b // s
    # end while
    return True


def Zadanie_55(a, b):
    for s in range(2, 17):
        if common_digit(a, b, s):
            print(s)
            break
    else:
        print("brak")



```