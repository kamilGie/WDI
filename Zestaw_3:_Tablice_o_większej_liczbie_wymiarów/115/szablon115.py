# ====================================================================================================>
# Zadanie 115
# Dwie liczby naturalne są ”wspólno-czynnikowe” jeżeli w swoich rozkładach na czynniki
# pierwsze mają dokładnie jeden wspólny czynnik. Na przykład: 24 i 21 albo 32 i 34. Dana jest tablica T[N][N]
# zawierająca liczby naturalne. Dwie liczby w tablicy sąsiadują ze sobą wtedy gdy leżą w tymm samym wierszu i
# sąsiednich kolumnach albo leżą w tej samej kolumnie i sąsiednich wierszach. Proszę napisać funkcję four(T),
# która zwraca ilość liczb sąsiadujących z 4 liczbami wspólno-czynnikowymi.
# ====================================================================================================>


def four(T): ...


if __name__ == "__main__":
    from testy115 import odpal_testy

    four(int(input('Podaj T: ')))

    # odpal_testy()
