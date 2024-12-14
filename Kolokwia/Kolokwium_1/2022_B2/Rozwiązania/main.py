# ====================================================================================================>
# Zadanie B2, 10.11.2022
# Dana jest kwadratowa tablica T wypełniona liczbami naturalnymi. Proszę napisać funkcję square(T), która
# znajdzie najmniejszy kwadratowy fragment tablicy, mniejszy niż cała tablica, taki że liczba będąca iloczynem
# czterech narożnych pól tego fragmentu w rozkładzie na czynniki pierwsze posiada tylko dwa różne czynniki.
# Funkcja powinna zwrócić rozmiar (bok) znalezionego kwadratu.
# Jeżeli kwadrat taki nie istnieje funkcja powinna zwrócić wartość 0
#  ====================================================================================================>
# przyjmuje ze bok to conjamniej 2


def dwa_rozne_czyniki(iloczyn):
    res = 0
    dzielnik = 2
    while iloczyn > 1:
        if iloczyn % dzielnik == 0:
            res += 1
            while iloczyn % dzielnik == 0:
                iloczyn //= dzielnik

            # Jeśli znaleźliśmy 2 dzielniki, sprawdzamy, czy w pełni podzieliły liczbę
            if res == 2:
                return iloczyn == 1

        dzielnik += 1

    return False  # byl jeden dzielnik tylko


def square(T):
    n = len(T)
    for bok in range(1, n - 1):  # Od 2x2 do największego możliwego
        for wiersz in range(n - bok):
            for kolumna in range(n - bok):
                iloczyn = (
                    T[wiersz][kolumna]
                    * T[wiersz][kolumna + bok]
                    * T[wiersz + bok][kolumna]
                    * T[wiersz + bok][kolumna + bok]
                )
                if dwa_rozne_czyniki(iloczyn):
                    return bok + 1
    return 0


