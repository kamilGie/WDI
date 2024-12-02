![Zadanie 50](../../srt/zbior_zadan/50.png)
```python
# Julia Smerdel
def fib_exists(num):
    a1, a2, b1, b2 = 1, 1, 1, 1
    fib_sum = 1

    while num != fib_sum:
        if num > fib_sum:
            fib_sum += a2
            a1, a2 = a2, a1 + a2
        if num < fib_sum:
            fib_sum -= b1
            b1, b2 = b2, b1 + b2
        if num < a2:
            break

    return num == fib_sum


def Zadanie_50(n):
    while fib_exists(n + 1):
        n += 1

    return n + 1

```