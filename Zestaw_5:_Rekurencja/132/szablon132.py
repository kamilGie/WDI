# ====================================================================================================>
# Zadanie 132
# Korzystając z zależności: symbol newtona(n|k) = symbol newtona(n-1|k-1) + symbol newtona(n-1|k)
# proszę napisać funkcję obliczającą wartość symbolu Newtona dla argumentów n i k.
# ====================================================================================================>


def Zadanie_132(n, k): ...


if __name__ == "__main__":
    from testy132 import odpal_testy

    Zadanie_132(int(input('Podaj n: ')), int(input('Podaj k: ')))

    # odpal_testy()
