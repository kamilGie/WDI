![Zadanie 82](../../srt/zbior_zadan/82.png)
```python
PREZYCJA = 100


def kwadrat_liczby_tablicowej(T: list):
    # mnozenie liczby tablicowej jesli przebije 10 cyfr wynik dajemy do nasten tablicy
    wynik = [0] * (len(T) * 2)
    for el1 in range(len(T)):
        for el2 in range(len(T)):
            mnozone_elementy = T[el1] * T[el2]
            wynik[el1 + el2] += mnozone_elementy
            wynik[el1 + el2 + 1] += wynik[el1 + el2] // 10000000000
            wynik[el1 + el2] %= 10000000000

    return wynik


def n_liczba_z_pierwiastka_z_2(n):

    # wynik bedzie tablica [1,14121356,237...]
    # wynik[0] = cyfra dziesietna np 1
    # wynik[1:] cyfry po przecinku po 10 cyfr
    wynik = [1]

    # metoda bisekcji szukanie liczb po przecinku
    while len(wynik) < PREZYCJA // 10 + 2:
        gora = 9999999999
        dol = 0
        # szukamy najwiekszego elementu dla ktorego kwadrat liczby staje sie 2 i bierzmy o jeden mniejszy
        while gora - dol > 1:
            domniemane_mniej_niz_2 = kwadrat_liczby_tablicowej( [(gora + dol) // 2] + wynik)
            cyfra_dziesietna = domniemane_mniej_niz_2[len(domniemane_mniej_niz_2) - 2]
            if cyfra_dziesietna == 1:
                dol = (gora + dol) // 2
            else:
                gora = (gora + dol) // 2

        # skladamy liczbe w tablice
        wynik = [dol] + wynik

    # szukanie w tablicy n miejsca po przecinku
    indeks = len(wynik) - 2
    n = n - 1
    while indeks >= 0:
        if n < 10:
            return int(str(wynik[indeks])[n])
        indeks -= 1
        n -= 10

```