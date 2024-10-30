# ====================================================================================================>
# Zadanie 2
# Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.
# ====================================================================================================>
# print(element_ciagu ,ends=' ')


def Zadanie_2():
    a = b = 1
    while a < 1e6:
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    from testy02 import odpal_testy

    Zadanie_2()

    # odpal_testy()
