# ====================================================================================================>
# Zadanie 12
# Proszę napisać program wypisujący rozkład liczby na czynniki pierwsze.
# ====================================================================================================>
# wypisac po spacji w jednej lini


def Czynniki(liczba):
    czynnik = 2  # (*)
    while czynnik * czynnik <= liczba:
        while liczba % czynnik == 0:  # (****)
            print(czynnik, end=" ")
            liczba = liczba // czynnik  # (***)
        czynnik += 1  # (**)
    if liczba > 1:
        print(liczba)  # (*****)


