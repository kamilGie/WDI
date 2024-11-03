# ====================================================================================================>
# Zadanie 33
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy jej
# cyfry stanowią ciąg geometryczny.
# ====================================================================================================>
# zadanie_33(124) --> return True


def Zadanie_33(n):
    if n // 10 == 0:
        return True

    iloczyn_ciagu = divmod
    while n > 0:
        n, d = divmod(n, 10)
        if ostatnie_d <= d:
            return False
        ostatnie_d = d
    return True


if __name__ == "__main__":
    from Develop import stworz_zadanie

    Zadanie_33()
    # stworz_zadanie([Zadanie_33])
