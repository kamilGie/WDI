# ====================================================================================================>
# Zadanie 6
# Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.
# ====================================================================================================>


# Pietryka
def Zadanie_6(n):
    a1 = 1
    a2 = (n / a1 + a1) * 0.5

    while abs(a2 - a1) > 1e-4:
        a1 = a2
        a2 = (n / a1 + a1) * 0.5

    print(int(a2))
