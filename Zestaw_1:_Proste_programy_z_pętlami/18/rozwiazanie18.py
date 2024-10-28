# ====================================================================================================>
# Zadanie 18
# Nieskończony iloczyn 0.5∗ 0.5+0.5∗ 0.5∗ 0.5+0.5∗ 0.5+0.5∗ 0.5 ∗... ma
# wartość 2/π. Proszę napisać program korzystający z tej zależności i wyznaczający wartość π.
# ====================================================================================================>
# return wartosci π


from math import sqrt


def Zadanie_18():

    a1 = sqrt(0.5)
    a2 = sqrt(0.5 + 0.5 * a1)
    iloczyn = a1 * a2

    while abs(a2 - a1) > 0.00000001:
        a1 = a2
        a2 = sqrt(0.5 + 0.5 * a1)
        iloczyn *= a2

    print(2 / iloczyn)


