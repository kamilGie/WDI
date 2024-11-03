# ====================================================================================================>
# Zadanie 36
# Proszę napisać program wyliczający pierwiastek równania x^x = 2020 metodą stycznych.
# ====================================================================================================>
# Zadanie_36() --> return x


from math import log


def f(x):
    return x**x - 2020


def df(x):
    return (x**x) * (log(x) + 1)


def solve():
    x = 1
    eps = 1e-4
    while abs(f(x)) > eps:
        x = x - f(x) / df(x)

    return x


