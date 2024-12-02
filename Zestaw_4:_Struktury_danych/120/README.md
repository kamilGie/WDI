![Zadanie 120](../../srt/zbior_zadan/120.png)
```python
def skr(num):
    x, y = num

    def nwd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    div = nwd(abs(x), abs(y))

    return x // div, y // div


def add(a, b):
    ans = (a[0] * b[1] + a[1] * b[0], a[1] * b[1])
    return skr(ans)


def subtract(a, b):
    ans = (a[0] * b[1] - a[1] * b[0], a[1] * b[1])
    return skr(ans)


def mult(a, b):
    ans = (a[0] * b[0], a[1] * b[1])
    return skr(ans)


def div(a, b):
    ans = (a[0] * b[1], a[1] * b[0])
    return skr(ans)


def exp(a, b):
    a = skr(a)
    ans = (a[0] ** b[0]) ** (1 / b[1]), (a[1] ** b[0]) ** (1 / b[1])
    return ans



```