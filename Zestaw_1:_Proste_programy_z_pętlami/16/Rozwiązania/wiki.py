# ====================================================================================================>
# Zadanie 16
# Proszę napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb
# naturalnych.
# ====================================================================================================>


def NWD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def NWW(a, b):
    return (a * b) // (NWD(a, b))


def NWW_3(a, b, c):
    return NWW(NWW(a, b), c)


