# ====================================================================================================>
# Zadanie 5
# Pierwiastekcałkowitoliczbowyzliczbynaturalnejtoczęśćcałkowitazpierwiastkaztejliczby.
# Proszę napisać program obliczający taki pierwiastek korzystając z zależności 1+3+5+...=n2.
# ====================================================================================================>


def Zadanie_5(n):
    suma = 0
    licznik = 0
    while suma + (licznik + 1) * 2 - 1 <= n:
        licznik += 1
        suma += licznik * 2 - 1

    return licznik


if __name__ == "__main__":

