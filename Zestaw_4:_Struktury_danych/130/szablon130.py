# ====================================================================================================>
# Zadanie 130
# Proszę napisać funkcję która dodaje dwie liczby wymierne reprezentowane jako rozwinięcia
# dziesiętne w postaci napisów na tak samo reprezentowaną liczbę wymierną. Na przykład suma ”0.25” i
# ”0.1(6)” daje ”0.41(6)”
# ====================================================================================================>


def Zadanie_130(liczba1: str, liczba2: str) -> str: ...


if __name__ == "__main__":
    from testy130 import odpal_testy

    Zadanie_130(str(input("Podaj liczba1: ")), str(input("Podaj liczba2: ")))

    # odpal_testy()
