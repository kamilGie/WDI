# ====================================================================================================>
# Zadanie 2
# Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.
# ====================================================================================================>


def Zadanie_2():
    b = a = 1
    while a < 1e6:
        print(a)
        b, a = a, a + b
