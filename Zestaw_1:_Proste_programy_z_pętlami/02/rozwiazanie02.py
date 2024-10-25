# ====================================================================================================>
# Zadanie 2
# Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.
# ====================================================================================================>


def Zadanie_2():
    a = b = 1
    while a < 1e6:
        print(a)
        a, b = b, a + b


