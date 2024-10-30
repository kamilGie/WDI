# ====================================================================================================>
# Zadanie 82
# Napisać program, który wyznacza n-tą cyfrę po przecinku rozwinięcia dziesiętnego wartości
# sqrt(2). Program powinien działać poprawnie dla n<100.
# ====================================================================================================>

PREZYCJA = 100


def wypisz_liczbe_tablicowa(T):
    indeks_liczby = len(T) - 1

    print(T[indeks_liczby], end=".")
    indeks_liczby -= 1
    while indeks_liczby >= 0:
        print(f"{int(T[indeks_liczby]):0>10}", end="")
        indeks_liczby -= 1
    print()


def kwadrat_liczby_tablicowej(T: list):
    wynik = [0] * (len(T) * 2)
    for el1 in range(len(T)):
        for el2 in range(len(T)):
            mnozone_elementy = T[el1] * T[el2]
            wynik[el1 + el2] += mnozone_elementy
            wynik[el1 + el2 + 1] += wynik[el1 + el2] // 10000000000
            wynik[el1 + el2] %= 10000000000

    return wynik


def n_liczba_z_pierwiastka_z_2(n):
    wynik = [1]

    while len(wynik) < PREZYCJA // 10 + 2:
        gora = 9999999999
        dol = 0
        while gora - dol > 1:
            domniemane_mniej_niz_2 = kwadrat_liczby_tablicowej(
                [(gora + dol) // 2] + wynik
            )
            cyfra_dziesietna = domniemane_mniej_niz_2[len(domniemane_mniej_niz_2) - 2]
            if cyfra_dziesietna == 1:
                dol = (gora + dol) // 2
            else:
                gora = (gora + dol) // 2

        wynik = [dol] + wynik

    indeks = len(wynik) - 2
    while indeks >= 0:
        if n < 10:
            return str(wynik[indeks])[n - 1]
        indeks -= 1
        n -= 10
