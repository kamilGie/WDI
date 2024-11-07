# ====================================================================================================>
# Zadanie 76
# Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w
# obu tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
# (z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
# sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+4+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
# i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
# tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum.
# ====================================================================================================>
# return liczba znalezionych sum  dajacych liczbe pierwsza


def maska_tritowa(t1, t2): ...


if __name__ == "__main__":
    from testy76 import odpal_testy

    maska_tritowa(int(input('Podaj t1: ')), int(input('Podaj t2: ')))

    # odpal_testy()
