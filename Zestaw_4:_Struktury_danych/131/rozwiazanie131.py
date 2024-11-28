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


def odejmij(liczba1, liczba2):
    c1, u1 = liczba1
    c2, u2 = liczba2

    if c2[0] == "-":
        return dodaj(liczba1, (c2[1:], u2))
    if c1[0] == "-":
        wynik_c, wynik_u = dodaj((c1[1:], u1), liczba2)
        return ("-" + wynik_c, wynik_u)
    if (c1 < c2) or (c1 == c2 and u1 < u2):
        wynik_c, wynik_u = odejmij(liczba2, liczba1)
        return ("-" + wynik_c, wynik_u)

    max_len = max(len(u1), len(u2))
    u1 = u1.ljust(max_len, "0")
    u2 = u2.ljust(max_len, "0")

    przeniesienie = 0
    wynik_u = ""
    for i in range(max_len - 1, -1, -1):
        różnica = int(u1[i]) - int(u2[i]) + przeniesienie
        if różnica < 0:
            różnica += 10
            przeniesienie = -1
        else:
            przeniesienie = 0
        wynik_u = str(różnica) + wynik_u

    wynik_u = wynik_u.rstrip("0") or "0"
    wynik_c = int(c1) - int(c2) + przeniesienie

    return (str(wynik_c), wynik_u)


def dodaj(liczba1, liczba2):
    c1, u1 = liczba1
    c2, u2 = liczba2

    if c1[0] == "-":
        return odejmij(liczba2, (c1[1:], u1))
    if c2[0] == "-":
        return odejmij(liczba1, (c2[1:], u2))

    max_len = max(len(u1), len(u2))
    u1 = u1.ljust(max_len, "0")
    u2 = u2.ljust(max_len, "0")

    przeniesienie = 0
    wynik_u = ""

    for i in range(max_len - 1, -1, -1):
        suma = int(u1[i]) + int(u2[i]) + przeniesienie
        przeniesienie, cyfra = divmod(suma, 10)
        wynik_u = str(cyfra) + wynik_u

    wynik_c = int(c1) + int(c2) + przeniesienie
    wynik_u = wynik_u.rstrip("0") or "0"

    return str(wynik_c), wynik_u


def pomnoz(liczba1, liczba2):
    c1, u1 = liczba1
    c2, u2 = liczba2

    if c1[0] == "-" and c2[0] == "-":
        return pomnoz((c1[1:], u1), (c2[1:], u2))
    elif c1[0] == "-" or c2[0] == "-":
        liczba_bez_znaku1 = (c1[1:], u1) if c1[0] == "-" else (c1, u1)
        liczba_bez_znaku2 = (c2[1:], u2) if c2[0] == "-" else (c2, u2)
        cw, uw = pomnoz(liczba_bez_znaku1, liczba_bez_znaku2)
        return ("-" + cw, uw)

    liczby_po_przecinku = len(u1) + len(u2)
    l1 = c1 + u1
    l2 = c2 + u2

    iloczyn = str(int(l1) * int(l2)).zfill(liczby_po_przecinku + 1)
    dziesietne = len(iloczyn) - liczby_po_przecinku
    return (iloczyn[:dziesietne] or "0", (iloczyn[dziesietne:].rstrip("0") or "0"))


