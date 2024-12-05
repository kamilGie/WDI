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


def dodaj(liczba1, liczba2):
    c1, u1 = liczba1
    l1 = float(str(c1) + "." + str(u1))
    c2, u2 = liczba2
    l2 = float(str(c2) + "." + str(u2))

    suma = str(l1 + l2)
    wc, wu = suma.split(".")

    return wc, wu


def odejmij(liczba1, liczba2):
    return dodaj(liczba1, ("-" + liczba2[0], liczba2[1]))


def pomnoz(liczba1, liczba2):
    c1, u1 = liczba1
    l1 = float(str(c1) + "." + str(u1))
    c2, u2 = liczba2
    l2 = float(str(c2) + "." + str(u2))

    suma = str(l1 * l2)
    wc, wu = suma.split(".")

    return wc, wu


if __name__ == "__main__":
    from testy131 import odpal_testy

    # dodaj(int(input("Podaj liczba1: ")), int(input("Podaj liczba2: ")))
    # odejmij(int(input("Podaj liczba1: ")), int(input("Podaj liczba2: ")))
    # pomnoz(int(input("Podaj liczba1: ")), int(input("Podaj liczba2: ")))

    odpal_testy()
