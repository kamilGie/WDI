# ====================================================================================================>
# Zadanie 4
# Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o za-
# danej sumie.
# ====================================================================================================>


def Zadanie_4(a):
    f1 = f2 = k1 = k2 = 1
    sum = 0

    while sum < a:
        sum += f1
        f1, f2 = f2, f1 + f2

    while sum > a:
        sum -= k1
        k1, k2 = k2, k1 + k2

    return sum == a


Zadanie_4(24)
