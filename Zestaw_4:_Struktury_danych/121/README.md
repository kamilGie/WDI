![Zadanie 121](../../srt/zbior_zadan/121.png)
```python
def skr(num):
    x, y = num

    def nwd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    div = nwd(abs(x), abs(y))

    return x // div, y // div


def subtract(a, b):
    ans = (a[0] * b[1] - a[1] * b[0], a[1] * b[1])
    return skr(ans)


def mult(a, b):
    ans = (a[0] * b[0], a[1] * b[1])
    return skr(ans)


def div(a, b):
    ans = (a[0] * b[1], a[1] * b[0])
    return skr(ans)


def Zadanie_121(a1, b1, c1, a2, b2, c2) -> tuple:
    """
    Metody Cramera z algerby

    https://www.matmana6.pl/twierdzenie-cramera

    """
    det_A = subtract(mult(a1, b2), mult(a2, b1))

    det_C1 = subtract(mult(c1, b2), mult(c2, b1))

    det_C2 = subtract(mult(a1, c2), mult(a2, c1))

    x = div(det_C1, det_A)
    y = div(det_C2, det_A)

    return x, y



```