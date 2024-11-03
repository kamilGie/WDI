# ====================================================================================================>
# Zadanie 35
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta zakończona jest unikalną cyfrą.
# ====================================================================================================>
# Zadanie_35(123) --> return True


def Zadanie_35(n):
    n, uniklana_cyfra = divmod(n, 10)
    while n > 0:
        n, liczba = divmod(n, 10)
        if liczba == uniklana_cyfra:
            return False
    return True


