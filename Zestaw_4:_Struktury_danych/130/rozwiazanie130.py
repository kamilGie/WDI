# ====================================================================================================>
# Zadanie 130
# Proszę napisać funkcję która dodaje dwie liczby wymierne reprezentowane jako rozwinięcia
# dziesiętne w postaci napisów na tak samo reprezentowaną liczbę wymierną. Na przykład suma ”0.25” i
# ”0.1(6)” daje ”0.41(6)”
# ====================================================================================================>


def skroc(licznik, mianownik):
    """szukanie nwd i skracanie przez niego"""
    a, b = licznik, mianownik
    while b != 0:
        a, b = b, a % b

    skorc_przez = a
    return (licznik // skorc_przez, mianownik // skorc_przez)


def Zadanie_129(liczba: str):
    """
    Funkcję która zamienia liczby wymierne reprezentowane jako rozwinięcia dziesiętne w postaci
    napisów na liczbę wymierną w postaci nieskracalnego ułamka jako pary licznik-mianownik.
    Na przykład: ”0.25” na (1,4), ”0.(6)” na (2,3), ”0.(142857)” na (1,7)
    """
    calkowite, po_przecinku = liczba.split(".")

    if "(" not in po_przecinku:
        mianownik = 10 ** len(po_przecinku)
        licznik = int(calkowite) * mianownik + int(po_przecinku)
    else:
        przed_okresem, okres = po_przecinku.split("(")
        okres = okres[:-1]

        mianownik_okres = 10 ** len(okres) - 1
        licznik_przed = int(przed_okresem) if przed_okresem else 0
        mianownik_przed = 10 ** len(przed_okresem)

        mianownik = mianownik_przed * mianownik_okres
        licznik = (
            int(calkowite) * mianownik + licznik_przed * mianownik_okres + int(okres)
        )

    return skroc(licznik, mianownik)


def Zadanie_130(liczba1: str, liczba2: str) -> str:
    """
    Konwertuje obie liczby na postać ułamkową, sumuje i skracam.
    Z tego ułamka obliczam część całkowitą.
    Następnie, dopóki część ułamkowa ma resztę lub reszta się nie powtórzy:
    - zapisuję w słowniku wystąpienie każdej reszty na określonej pozycji
    - tworzę nową resztę, mnożąc ją przez 10 i dzieląc przez mianownik.
    Jeśli reszta się powtarza, oznacza to, że mamy okres. Zwracam wynik z częścią całkowitą,
    częścią ułamkową przed okresem oraz samym okresem w nawiasach.
    Jeśli reszta się wyzeruje, zwracam część całkowitą z ułamkiem.
    """

    l1, m1 = Zadanie_129(liczba1)
    l2, m2 = Zadanie_129(liczba2)
    licznik, mianownik = skroc(l1 * m2 + l2 * m1, m1 * m2)

    calkowite = str(licznik // mianownik)

    reszta = licznik % mianownik
    reszty = {}
    ulamek = ""
    while reszta:
        reszty[reszta] = len(ulamek)

        ulamek += str(reszta * 10 // mianownik)
        reszta = reszta * 10 % mianownik
        if reszta in reszty:
            przed_okresem = ulamek[: reszty[reszta]]
            okres = ulamek[reszty[reszta] :]
            return f"{calkowite}.{przed_okresem}({okres})"

    return calkowite + "." + (ulamek or "0")
