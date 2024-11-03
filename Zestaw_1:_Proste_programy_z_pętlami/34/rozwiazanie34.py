# ====================================================================================================>
# Zadanie 34
# Proszę napisać programw czytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta zawiera cyfrę równą liczbie swoich cyfr.
# ====================================================================================================>

import math


def Zadanie_34(n):
    liczba_cyfr = math.floor(math.log10(n)) + 1

    if liczba_cyfr > 9:
        return False

    while n > 0:
        n, d = divmod(n, 10)
        if d == liczba_cyfr:
            return True

    return False


