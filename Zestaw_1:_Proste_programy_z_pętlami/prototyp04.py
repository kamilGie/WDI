# ====================================================================================================>
# Zadanie 4
# Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o za-
# danej sumie.
# ====================================================================================================>


def Zadanie_5(n):
    suma = 0
    licznik = 0
    while suma + (licznik + 1) * 2 - 1 <= n:
        licznik += 1
        suma += licznik * 2 - 1

    return licznik


if __name__ == "__main__":
    from Develop import stworz_zadanie

    stworz_zadanie([Zadanie_5])
