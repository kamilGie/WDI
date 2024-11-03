# ====================================================================================================>
# Zadanie 33
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy jej
# cyfry stanowią ciąg geometryczny.
# ====================================================================================================>
# zadanie_33(124) --> return True


def Zadanie_33(n):
    if n < -9:
        return False
    if n < 10 == 0:
        return True

    n, ostatnie_d = divmod(n, 10)
    n, d = divmod(n, 10)
    iloczyn_ciagu = ostatnie_d / d if d != 0 else 0
    print(iloczyn_ciagu)
    ostatnie_d = d
    while n > 0:
        n, d = divmod(n, 10)
        if d * iloczyn_ciagu != ostatnie_d:
            return False
        ostatnie_d = d
    return True


