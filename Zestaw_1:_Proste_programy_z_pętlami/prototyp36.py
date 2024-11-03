# ====================================================================================================>
# Zadanie 36
# Proszę napisać program wyliczający pierwiastek równania x^x = 2020 metodą stycznych.
# ====================================================================================================>
# Zadanie_36() --> return x

# odp z wiki
# nie dziala xd


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


if __name__ == "__main__":
    from Develop import stworz_zadanie

    solve()
    # stworz_zadanie([solve], strategia="tfloat")
