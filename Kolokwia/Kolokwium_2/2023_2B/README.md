
![black_Zrzut ekranu 2024-12-3 o 23 21 26](https://github.com/user-attachments/assets/a3a00dd6-7a9c-4010-8711-eeff35d3b53c)

```python
from math import isqrt


def a(n):
    res = 1
    if n == 1:
        return res
    for i in range(2, isqrt(n)):
        if n % i == 0:
            res += i
            res += n // i

    if isqrt(n) ** 2 == n:
        res += isqrt(n)
    return res


def b(n):
    a, b = 1, 1
    while a <= n:
        a, b = a + b, a
    return a


def c(n):
    # return n + int(str(n)[::-1])
    reverse = 0
    kopia = n
    while kopia > 0:
        kopia, d = divmod(kopia, 10)
        reverse = reverse * 10 + d
    return n + reverse


def cycle(x, n):
    def rek(l, i):
        if l == x:
            return n - i  # powrocila
        if i == 0:
            return 0
        return max(rek(a(l), i - 1), rek(b(l), i - 1), rek(c(l), i - 1))

    # zwracam max dlugosci łańcucha jesli nie bedzie zadnego to max zwróci 0
    return max(rek(a(x), n - 1), rek(b(x), n - 1), rek(c(x), n - 1))

```
