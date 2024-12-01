# ====================================================================================================>
# Zadanie 168
# Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza
# czy jest możliwe pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawał-
# ków też była liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Naprzykład: divide(2347)=True,
# podział na 23 i 47, natomiast divide(2255)=False.
# Przykładowe wywołania funkcji:
# print(divide(273)) # True, podział 2|7|3
# print(divide(22222)) # True, podział 2|2|2|2|2
# print(divide(23672)) # True, podział 23|67|2
# print(divide(2222)) # False
# print(divide(21722)) # False
# ====================================================================================================>

from math import log10, floor, isqrt


def czy_pierwsza(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def istnieja_kawalki(n, ilosci_kawalkow):
    """
    Po kolei, odcinając po jednej cyfrze, sprawdzam, czy odcięty kawałek
    jest liczbą pierwszą. Jeśli tak, wywołuję funkcję rekurencyjnie z pozostałością
    liczby nieodciętej oraz jeden mniej wymaganym kawałkiem.

    Gdy liczba kawałków wynosi 1, oznacza to, że cała liczba musi być
    liczbą pierwszą. Jeśli jest, to istnieją takie kawałki.
    """

    if ilosci_kawalkow == 1:
        return czy_pierwsza(n)

    kawalek = 0
    mnoznik = 1
    while n > 0:
        n, d = divmod(n, 10)
        kawalek += d * mnoznik
        mnoznik *= 10
        if czy_pierwsza(kawalek) and istnieja_kawalki(n, ilosci_kawalkow - 1):
            return True

    return False


def divide(N):
    """
    Dla liczb od 2 do dlugosci N sprawdzam czy jest liczba pierwsza oraz czy istnieje podzial
    liczby N na i czesci
    """
    for i in range(2, floor(log10(N)) + 2):
        if czy_pierwsza(i) and istnieja_kawalki(N, i):
            return True
    return False


