# ====================================================================================================>
# Zadanie 60
# Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.
# ====================================================================================================>
# print(dwojkowa, end=" ")
# print(trojkowa, end=" ")
# Zadanie_60(15) -> print(1111 120 33 30 23 21 17 16 15 14 13 12 11 10 F)


def zamien_na_system(liczba, podstawa):
    znaki = "0123456789ABCDEF"
    wynik = ""

    while liczba > 0:
        reszta = liczba % podstawa
        wynik = znaki[reszta] + wynik
        liczba //= podstawa

    return wynik or "0"


def Zadanie_60(liczba):
    for i in range(2, 17):
        print(zamien_na_system(liczba, i), end=" ")


