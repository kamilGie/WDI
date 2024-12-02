# ====================================================================================================>
# Zadanie 22
# Proszę napisać program wyznaczający wartość liczby e korzystając z zależności: e=1/0!+
# 1/1!+1/2!+1/3!+...
# √
# ====================================================================================================>
# return e


def Zadanie_22():
    e = 0
    n = 0
    silnia = 1
    wzrost = 1
    while wzrost > 1e-6:
        wzrost = 1 / silnia
        e += wzrost
        n += 1
        silnia = silnia * n
    return e
