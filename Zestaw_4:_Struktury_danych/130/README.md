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
    l1, m1 = Zadanie_129(liczba1)
    l2, m2 = Zadanie_129(liczba2)
    licznik, mianownik = skroc(l1 * m2 + l2 * m1, m1 * m2)

    calkowite = str(licznik // mianownik)

    reszta = licznik % mianownik
    # slownik z pozycja wystapieniem reszt
    reszty = {}
    ulamek = ""
    while reszta:
        reszty[reszta] = len(ulamek)

        ulamek += str(reszta * 10 // mianownik)
        reszta = reszta * 10 % mianownik
        if reszta in reszty: # reszta sie powtorzyla
            przed_okresem = ulamek[: reszty[reszta]]
            okres = ulamek[reszty[reszta] :]
            return f"{calkowite}.{przed_okresem}({okres})"

    return calkowite + "." + (ulamek or "0")

```
# Opis Rozwiązania
## `Zadanie_130`
Konwertuje obie liczby na postać ułamkową, sumuje i skracam.

Z tego ułamka obliczam część całkowitą jako `calkowite`

Następnie, dopóki `ułamek` ma resztę lub reszta się nie powtórzy:
- zapisuję w słowniku `reszty` wystąpienie każdej `reszta` na określonej pozycji
- tworzę nową `reszta`, mnożąc ją przez 10 i dzieląc przez `mianownik`.

Jeśli `reszta` się powtarza, oznacza to, że mamy okres. Zwracam wynik z częścią całkowitą, częścią ułamkową przed okresem oraz samym okresem w nawiasach.

Jeśli reszta się wyzeruje, zwracam część całkowitą z ułamkiem.
## `Zadanie_129`
Funkcję która zamienia liczby wymierne reprezentowane jako rozwinięcia dziesiętne w postaci
napisów na liczbę wymierną w postaci nieskracalnego ułamka jako pary licznik-mianownik.
Na przykład: ”0.25” na (1,4), ”0.(6)” na (2,3), ”0.(142857)” na (1,7)
