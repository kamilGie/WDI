# ====================================================================================================>
# Zadanie B2, 10.11.2022
# Dana jest kwadratowa tablica T wypełniona liczbami naturalnymi. Proszę napisać funkcję square(T), która
# znajdzie najmniejszy kwadratowy fragment tablicy, mniejszy niż cała tablica, taki że liczba będąca iloczynem
# czterech narożnych pól tego fragmentu w rozkładzie na czynniki pierwsze posiada tylko dwa różne czynniki.
# Funkcja powinna zwrócić rozmiar (bok) znalezionego kwadratu.
# Jeżeli kwadrat taki nie istnieje funkcja powinna zwrócić wartość 0
#  ====================================================================================================>
# przyjmuje ze bok to conjamniej 2


def square(T): ...


if __name__ == "__main__":
    from testy2022_B2 import odpal_testy

    square([[2, 3, 5], [1, 1, 13], [2, 6, 23]])  # return 2

    # odpal_testy()
