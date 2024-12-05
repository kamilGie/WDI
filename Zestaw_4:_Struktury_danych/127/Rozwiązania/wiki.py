# ====================================================================================================>
# Zadanie 127
# Napis nazywamy wielokrotnym, jeżeli powstał przez n-krotne (n>1) powtórzenie innego
# napisu o długości conajmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA.
# Dana jest tablica T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuższego
# napisu wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy.
# ====================================================================================================>


def multi(T):
    najdluzszy_cykl = 0
    for napis in T:
        n = len(napis)

        # Przeszukiwanie od połowy długości napisu w dół
        for dlugosc_cyklu in range(n // 2, 0, -1):
            # Sprawdzenie, czy długość napisu jest podzielna przez dlugosci_cyklu
            if n % dlugosc_cyklu == 0:
                # Sprawdzenie, czy podnapis o długości `dlugosc_cyklu` powtarzany `liczba_powtorzen` razy tworzy oryginalny napis
                fragment = napis[:dlugosc_cyklu]
                liczba_powtorzen = n // dlugosc_cyklu
                if fragment * liczba_powtorzen == napis:
                    najdluzszy_cykl = max(najdluzszy_cykl, dlugosc_cyklu)
                    break
    return najdluzszy_cykl
