# ====================================================================================================>
# Zadanie 144
# Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym
# iloczynie.
# ====================================================================================================>
# return liczba enek


def Zadanie_144(tablica, okreslony_iloczyn, liczba_elementow): ...


if __name__ == "__main__":
    from testy144 import odpal_testy

    Zadanie_144(int(input('Podaj tablica: ')), int(input('Podaj okreslony_iloczyn: ')), int(input('Podaj liczba_elementow: ')))

    # odpal_testy()
