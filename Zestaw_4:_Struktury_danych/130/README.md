<picture>
  <source srcset="../../srt/zbior_zadan/130.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_130.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_130.png" alt="zadanie 130">
</picture>

```python
def skroc(licznik, mianownik):
    """szukanie nwd i skracanie przez niego"""
    a, b = licznik, mianownik
    while b != 0:
        a, b = b, a % b

    skorc_przez = a
    return (licznik // skorc_przez, mianownik // skorc_przez)


def Zadanie_129(liczba: str):
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
    # Konwertuje obie liczby na postać ułamkową, sumuje i skracam.
    l1, m1 = Zadanie_129(liczba1)
    l2, m2 = Zadanie_129(liczba2)
    licznik, mianownik = skroc(l1 * m2 + l2 * m1, m1 * m2)

    # Z ułamka obliczam część całkowitą jako
    calkowite = str(licznik // mianownik)

    reszta = licznik % mianownik
    # slownik z pozycja wystapieniem reszt
    reszty = {}
    ulamek = ""

    while reszta:
        # zapisuję w słowniku `reszty` wystąpienie każdej `reszta` na określonej pozycji
        reszty[reszta] = len(ulamek)

        # sprawdzam następną resztę
        ulamek += str(reszta * 10 // mianownik)
        reszta = reszta * 10 % mianownik
        if reszta in reszty: # reszta sie powtórzyła
            przed_okresem = ulamek[: reszty[reszta]]
            okres = ulamek[reszty[reszta] :]
            return f"{calkowite}.{przed_okresem}({okres})"

    # reszta się wyzerowała, zwracam część całkowitą z ułamkiem.
    return calkowite + "." + (ulamek or "0")

```
