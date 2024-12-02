![Zadanie 04](../../srt/zbior_zadan/04.png)
```python
def is_in_fib(a):
    f1 = f2 = k1 = k2 = 1
    sum = 0

    while sum < a:
        sum += f1
        f1, f2 = f2, f1 + f2

    while sum > a:
        sum -= k1
        k1, k2 = k2, k1 + k2

    return sum == a



```