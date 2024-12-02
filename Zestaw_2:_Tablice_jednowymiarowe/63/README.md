![Zadanie 63](../../srt/zbior_zadan/63.png)
```python
def long_div(a, b, t):
    t[0] = a // b
    a = a % b
    for i in range(1, len(t)):
        a = a * 10
        t[i] = a // b
        a = a % b
        if a == 0:
            return t

    return t


def Zadanie_63(n):
    n = n + 2
    digits = [1] + [0] * (n)
    tab = [0] * (n + 1)
    fact = 1
    k = 1

    while fact <= 10**n + 1:
        fact *= k
        k += 1
        long_div(1, fact, tab)
        for i in range(n + 1):
            digits[i] += tab[i]

    for i in range(len(digits) - 1, 0, -1):
        digits[i - 1] += digits[i] // 10
        digits[i] %= 10

    print(digits[0], end=".")
    for cyfra in digits[1:-2]:
        print(cyfra, end="")



```