# ====================================================================================================>
# Zadanie 9
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.
# ====================================================================================================>


def iloczyn(liczba):
    a, b = 1, 1
    while a * b < liczba:
        a, b = b, a + b

    return a * b == liczba


