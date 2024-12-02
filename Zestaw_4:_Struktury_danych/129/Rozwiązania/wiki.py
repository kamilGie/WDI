# ====================================================================================================>
# Zadanie 129
# Proszę napisać funkcję która zamienia liczby wymierne reprezentowane jako rozwinię-
# cia dziesiętne w postaci napisów na liczbę wymierną w postaci nieskracalnego ułamka jako pary licznik-
# mianownik. Na przykład: ”0.25” na (1,4), ”0.(6)” na (2,3), ”0.(142857)” na (1,7)
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
    1. Funkcja dzieli liczbę na część całkowitą i część dziesiętną (po przecinku).
    2. Jeśli część dziesiętna nie zawiera okresu (czyli nie ma nawiasu `()`), obliczamy odpowiedni licznik i mianownik na podstawie liczby po przecinku.
    3. Jeśli część dziesiętna zawiera okres (np. "0.(3)"), dzielimy ją na część przed okresem i okres.
       - Mianownik dla części okresowej obliczamy jako liczbę składającą się z dziewiątek (np. dla okresu o długości 1 to "9", dla okresu o długości 2 to "99").
       - Licznik dla okresu to wartość tego okresu pomnożona przez odpowiedni mianownik.
       - Licznik dla części przed okresem jest liczony podobnie jak w przypadku liczby bez okresu, ale musi być pomnożony przez odpowiedni mianownik uwzględniający obecność okresu.
    4. Licznik końcowy obliczamy jako sumę trzech składników:
       - Liczba całkowita pomnożona przez odpowiedni mianownik.
       - Licznik dla części przed okresem.
       - Licznik dla części okresowej.
    5. Wynik zwracany jest w postaci skróconego ułamka
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


