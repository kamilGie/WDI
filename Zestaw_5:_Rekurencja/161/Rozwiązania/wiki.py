# vglorm
# ====================================================================================================>
# Zadanie 161
# Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję,
# która zwraca informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym
# podzbiorze, łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była
# jednakowa. Na przykład: [2,3,5,7,15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
# [5,7,15]→false, podział nie istnieje.
# ====================================================================================================>


def policz_jedynki_binarnie(liczba):
    licznik = 0
    while liczba > 0:
        licznik += liczba % 2
        liczba //= 2
    return licznik


def Zadanie_161(T):
    # Przechowuje liczbe jedynek w zapisie binarnym każdej liczby z T.
    tablica_jedynek = [policz_jedynki_binarnie(x) for x in T]

    # Jeśli podzbiór ma istnieć, suma całej `tablicy_jedynek` musi być podzielna przez 3
    suma_jedynek = sum(tablica_jedynek)
    if suma_jedynek % 3 != 0:
        return False

    # dzielenia sumy przez 3 będzie docelową sumą dla każdego podzbioru.
    cel = suma_jedynek // 3

    def czy_mozna_podzielic(A, B, C, indeks):
        """Rekurencyjnie tworzę 3 sumy: `A`, `B`, `C`. Dodając do każdej z nich wartości z `tablicy_jedynek`"""

        # Jeśli uda się rozdzielić wszystkie elementy z tablicy jedynek i nie przekroczyć docelowej sumy, to podział jest możliwy.
        if indeks == len(T):
            return True

        liczba = tablica_jedynek[indeks]

        # Sprawdzam czy jakaś kombinacja pozwoli rozdzielić liczbe tak, aby suma  nie przekroczyła docelowej wartości.
        if A + liczba <= cel and czy_mozna_podzielic(A + liczba, B, C, indeks + 1):
            return True
        if B + liczba <= cel and czy_mozna_podzielic(A, B + liczba, C, indeks + 1):
            return True
        if C + liczba <= cel and czy_mozna_podzielic(A, B, C + liczba, indeks + 1):
            return True

        return False

    return czy_mozna_podzielic(0, 0, 0, 0)
