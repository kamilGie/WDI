# ====================================================================================================>
# Zadanie 95
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.
# ====================================================================================================>
# return najwiekszy_iloraz
# ratio_check_in_tab([[1, 2, 3], [4, 5, 6], [7, 8, 9]] - > return 3.0


def ratio_check_in_tab(tab): ...


if __name__ == "__main__":
    from testy095 import odpal_testy

    ratio_check_in_tab(int(input("Podaj tab: ")))

    # odpal_testy()
