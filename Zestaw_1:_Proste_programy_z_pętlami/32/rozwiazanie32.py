# ====================================================================================================>
# Zadanie 32
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy jej
# cyfry stanowią ciąg rosnący.
# ====================================================================================================>


def Zadanie_32(n):
    ostatnie_d = 10
    while n > 0:
        n, d = divmod(n, 10)
        if ostatnie_d <= d:
            return False
        ostatnie_d = d
    return True


