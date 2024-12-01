# ====================================================================================================>
# Zadanie 170
# Dana jest funkcja Ackermana, określona na zbiorze liczb całkowitych nieujemnych, dana
# wzorem rekurencyjnym:
# def f(a,b):
#    if a==0: return b+1
#    if b==0: return f(a-1,1)
#    return f (a-1,f(a,b-1))
# Proszę napisać funkcję w wersji iteracyjnej.
# ====================================================================================================>


def Zadanie_170(a, b): ...


if __name__ == "__main__":
    from testy170 import odpal_testy

    Zadanie_170(int(input("Podaj a: ")), int(input("Podaj b: ")))

    odpal_testy()
