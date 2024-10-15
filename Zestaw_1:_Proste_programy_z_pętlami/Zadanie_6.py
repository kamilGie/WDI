# ====================================================================================================>
# Zadanie 6
# Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.
# ====================================================================================================>


def Zadanie_6(s):
    a1 = 1
    a2 = (s / a1 + a1) / 2
    epsilon = 1e-5

    while abs(a2 - a1) > epsilon:
        a1 = a2
        a2 = (s / a1 + a1) / 2

    print(a2)


Zadanie_6(float(input()))
