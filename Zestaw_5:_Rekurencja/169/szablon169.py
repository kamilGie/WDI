# ====================================================================================================>
# Zadanie 169
# Dwie liczby naturalne są ”wspólno-czynnikowe” jeżeli w swoich rozkładach na czynniki
# pierwsze mają dokładnie jeden wspólny czynnik. Na przykład: 24 i 21 albo 32i 34.Dana jest tablicaT[N][N]
# zawierająca liczbynaturalne. Dwie liczby w tablicy sąsiadują ze sobą wtedy gdy leżą w tym samym wierszu i
# sąsiednich kolumnach albo leżą w tej samej kolumnie i sąsiednich wierszach. Proszę napisać funkcję four(T),
# która zwraca ilość liczb sąsiadujących z 4 liczbami wspólno-czynnikowymi.
# ====================================================================================================>


def four(T): ...


if __name__ == "__main__":
    from testy169 import odpal_testy

    four(list(input("Podaj T: ")))

    # odpal_testy()
