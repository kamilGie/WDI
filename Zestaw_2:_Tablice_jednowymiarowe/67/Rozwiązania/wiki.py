# ====================================================================================================>
# Zadanie 67
# Dana jest N-elementowa tablica T zawierająca liczby naturalne. W tablicy możemy przeskoczyć
# z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby T[k]. Napisać
# funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.
# ====================================================================================================>
# return true jak moze lub false jak nie moze

from math import isqrt


def isprime(n) -> bool:
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def get_czynniki(liczba) -> list:
    return [a for a in range(2, liczba + 1) if isprime(a) and liczba % a == 0]


def Zadanie_67(T) -> bool:
    Can_jump = [False for _ in range(len(T))]
    Can_jump[0] = True
    a = 0
    while a < len(T):
        if Can_jump[a] == True:
            for czynnik in get_czynniki(T[a]):
                if czynnik + a < len(T):
                    Can_jump[a + czynnik] = True
                    if Can_jump[-1] == True:
                        return Can_jump[-1]
        a += 1
    return Can_jump[-1]


