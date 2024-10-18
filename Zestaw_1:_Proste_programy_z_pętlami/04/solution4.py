# ====================================================================================================>
# Zadanie 4
# Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o za-
# danej sumie.
# ====================================================================================================>


# https://github.com/pawlowiczf/WDI-2023/blob/main/WDI%20zestaw%201/3.py
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


# Gieras 3 zmienne
def Zadanie_4(n):
    a = b = 1

    while a - 1 < n:
        a, b = b, a + b

    n = (a - 1) - n
    a = b = 1
    while a - 1 < n:
        a, b = b, a + b

    return a - 1 == n
