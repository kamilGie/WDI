# ====================================================================================================>
# Zadanie 31
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3*(An-1) +1, a pierwszy wyraz jest
# równy 2.
# ====================================================================================================>


def czy_ciag(n): ...


if __name__ == "__main__":
    from testy31 import odpal_testy

    czy_ciag(int(input('Podaj n: ')))

    # odpal_testy()
