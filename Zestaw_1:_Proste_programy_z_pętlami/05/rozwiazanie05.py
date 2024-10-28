# ====================================================================================================>
# Zadanie 5
# Pierwiastekcałkowitoliczbowyzliczbynaturalnejtoczęśćcałkowitazpierwiastkaztejliczby.
# Proszę napisać program obliczający taki pierwiastek korzystając z zależności 1+3+5+...=n2.
# ====================================================================================================>
# return (pierwiastek)


def Zadanie_5(liczba: int):
    suma = 0
    licznik = 0
    nieparzysta = 1

    while suma <= liczba:
        suma += nieparzysta
        nieparzysta += 2
        licznik += 1

    return licznik - 1


