# ====================================================================================================>
# Zadanie 25
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.
# ====================================================================================================>
# return True albo False


from math import sqrt


def Zadanie_25(n):
    a1, a2 = 1, 1

    while a1 < sqrt(n) + 1:
        if n % a1 == 0:
            b1, b2 = a1, a2

            while a1 * b1 < n:
                b1, b2 = b2, b1 + b2

            if a1 * b1 == n:
                return True

        a1, a2 = a2, a1 + a2

    return False


