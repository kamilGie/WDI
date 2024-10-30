# ====================================================================================================>
# Zadanie 82
# Napisać program, który wyznacza n-tą cyfrę po przecinku rozwinięcia dziesiętnego wartości
# sqrt(2). Program powinien działać poprawnie dla n<100.
# ====================================================================================================>

PRECYZJA = 1000


def kwadrat_liczby_tablicowej(T):
    wynik = [0] * (len(T) * 2)
    for el1 in range(len(T)):
        for el2 in range(len(T)):
            mnożone_elementy = T[el1] * T[el2]
            wynik[el1 + el2] += mnożone_elementy
            wynik[el1 + el2 + 1] += wynik[el1 + el2] // 10000000000
            wynik[el1 + el2] %= 10000000000

    return wynik


def n_liczba_z_pierwiastka_z_2(n):
    # Pierwiastek będzie odwroconą tablicą
    # Jego liczby będą zapisywane po 10 liczb
    # [4142135623, 1, 0]
    # Zero na początku jest dodane, aby mnożenie działało
    wynik = [1, 0]

    while len(wynik) < PRECYZJA // 10 + 2:
        gora = 9999999999
        dol = 0
        while gora - dol > 1:
            liczba = (gora + dol) // 2
            # Sprawdzamy, czy z tej liczby kwadrat nie daje liczby większej niż 1
            # Jeśli tak, to oznacza, że jest to za duża liczba i zmniejszamy górę
            domniemane_mniej_niz_2 = kwadrat_liczby_tablicowej([liczba] + wynik)
            cyfra_dziesietna = domniemane_mniej_niz_2[len(domniemane_mniej_niz_2) - 2]
            if cyfra_dziesietna == 1:
                dol = liczba
            else:
                gora = liczba

        wynik = [dol] + wynik

    indeks = len(wynik) - 2
    while indeks >= 0:
        if n < 10:
            return str(wynik[indeks])[n - 1]
        indeks -= 1
        n -= 10
