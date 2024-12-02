# ====================================================================================================>
# Zadanie 6
# Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.
# ====================================================================================================>


def Zadanie_6(s):

    ε = 1e-6
    a1 = 1
    a2 = (s / a1 + a1) * 0.5

    while abs(a2 - a1) > ε:
        a1 = a2
        a2 = (s / a1 + a1) * 0.5

    return a2
