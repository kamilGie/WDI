# ====================================================================================================>
# Zadanie 131
# Liczby rzeczywiste są reprezentowane w postaci krotek(c,u), gdzie c jest częścią całkowitą
# liczby, a u jest liczbą całkowitą utworzoną z cyfr po przecinku. Na przykład krotka(6,23)reprezentuje liczbę
# 6.23. Proszę napisać następujące funkcje:
# • Dodającą dwie liczby,
# • Odejmującą dwie liczby,
# • Mnożącą dwie liczby.
# ====================================================================================================>
# c,u sa stringami aby moc zapisac np 0.05
# -1.2 to bedzie np ("-1","2")
# -0.3 to bedzie ("-0","3")


def odejmij(liczba1, liczba2): ...


def dodaj(liczba1, liczba2): ...


def pomnoz(liczba1, liczba2): ...


if __name__ == "__main__":
    from testy131 import odpal_testy

    dodaj(int(input("Podaj liczba1: ")), int(input("Podaj liczba2: ")))
    odejmij(int(input("Podaj liczba1: ")), int(input("Podaj liczba2: ")))
    pomnoz(int(input("Podaj liczba1: ")), int(input("Podaj liczba2: ")))

    # odpal_testy()
