def f(x):
    return x**x - 2020


def solve(ep = 0.0000001):
    a, b = 0, 100
    while abs(a-b) > ep:
        x = (a+b)/2
        if f(x) == 0:
            return x
        if f(a)*f(x) < 0:
            b = x
        elif f(x)*f(b) < 0:
            a = x
    return (a+b)/2


print(solve())