![Zadanie 36](../../srt/zbior_zadan/36.png)
```python
import math


def solve(f, df):
    x = 1
    eps = 0.0001
    prev_x = x + eps * 10
    while abs(prev_x - x) > eps:
        prev_x = x
        x = x - f(x) / df(x)

    print(x)


def function(x):
    return x**x - 2020


def derivative(x):
    return (x**x) * (math.log(x) + 1)


# OR


def log_function(x):
    return x * math.log(x) - math.log(2020)


def log_derivative(x):
    return math.log(x) + 1

```