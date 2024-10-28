# ====================================================================================================>
# Zadanie 10
# Proszę napisać program sprawdzający czy zadana liczba jest pierwszą.
# ====================================================================================================>


def Zadanie_10(liczba: int): ...


if __name__ == "__main__":
    from testy10 import odpal_testy

    print(Zadanie_10(int(input("Podaj liczba: "))))

    # odpal_testy()
