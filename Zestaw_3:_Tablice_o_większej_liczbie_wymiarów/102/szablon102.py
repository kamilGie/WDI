# ====================================================================================================>
# Zadanie 102
# Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
# są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
# naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z
# przyjaciółkami
# ====================================================================================================>
# return ilosci
# Zadanie_102([1,1,1][1,1,1][1,1,1]) --> return 9


def Zadanie_102(T): ...


if __name__ == "__main__":
    from testy102 import odpal_testy

    Zadanie_102(int(input('Podaj T: ')))

    # odpal_testy()
