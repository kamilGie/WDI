# ====================================================================================================>
# Zadanie 33
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy jej
# cyfry stanowią ciąg geometryczny.
# ====================================================================================================>
# zadanie_33(124) --> return True
# nie wychodzi


def Zadanie_33(n):
    if n < 10:
        return True

    ostatnia, n = n % 10, n // 10
    przedostatnia = n % 10
    if ostatnia == 0 or przedostatnia == 0:
        return False

    r = ostatnia / przedostatnia
    while n >= 10:
        ostatnia, n = przedostatnia, n // 10
        przedostatnia = n % 10
        if ostatnia == 0 or przedostatnia == 0 or ostatnia / przedostatnia != r:
            return False

    return True


