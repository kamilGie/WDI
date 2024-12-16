# ====================================================================================================>
# Zadanie 2B, 16.12.2024
#
# Dane są trzy operacje: A, B, C przekształcające liczbę naturalną x na inną liczbę naturalną.
#
# • A zamienia liczbę x na jej rewers i dodaje 1. Na przykład: 123 → 322, 230 → 33.
# • B zamienia liczbę x na najmniejszą liczbę pierwszą większą od x. Na przykład: 13 → 17, 20 → 23.
# • C oblicza odwrotność liczby x i zwraca liczbę złożoną z 3 cyfr rozwinięcia dziesiętnego odwrotności, po
#   pominięciu początkowych zer. Na przykład: 6 → 166 bo 1/6 = 0.16666..., 10 → 100 bo 1/10 = 0.1000...,
#   12 → 833 bo 1/12 = 0.083333..., 997 → 100 bo 1/997 = 0.001003009...
#
# Proszę napisać funkcję cykl(x), która dla liczby naturalnej x zwraca minimalną sekwencję operacji, których
# wykonanie powraca do liczby początkowej x. Do funkcji należy przekazać wyłącznie wartość początkową x,
# funkcja powinna zwrócić napis złożony z liter A, B, C. Jeżeli nie jest możliwy powrót do wartości początkowej
# w mniej niż 10 operacjach, funkcja powinna zwrócić napis pusty. Można założyć, że x <= 10^6.
#
# Przykłady:
# cykl(3)="BCA", 3 → 5 → 200 → 3,
# cykl(35)="BBBA", 35 → 37 → 41 → 43 → 35,
# cykl(45)="CABCA", 45 → 222 → 223 → 227 → 440 → 45,
# cykl(51)="", cykl krótszy niż 10 nie istnieje.
# ====================================================================================================>

from math import isqrt


def isprime(x):
    """sprawdza czy liczby wieksze od 1 sa pierwsze"""
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, isqrt(x) + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True


def a(x):
    res = 0
    while x > 0:
        x, d = divmod(x, 10)
        res = res * 10 + d
    return res + 1


def b(x):
    while True:
        x += 1
        if isprime(x):
            return x


def c(x):
    res = 1 / x
    while int(res) == 0:  # usuwanie zer z przodu
        res *= 10
    return int(res * 100)  # 3 cyfry rozwiniecia


def cykl(x):
    def rek(l, i):
        if i == 10:  #  za dlugi
            return ""
        if l == x and i > 0:  # sukces
            return ""

        na = "A" + rek(a(l), i + 1)
        nb = "B" + rek(b(l), i + 1)
        nc = "C" + rek(c(l), i + 1)
        return min(na, nb, nc, key=len)  # najmniejszy napis

    res = rek(x, 0)
    return ( res if len(res) < 10 else "")  # jesli napis jest krotszy niz 10 to znaleziono taki cykl


