# ====================================================================================================>
# Zadanie 125
# Liczby zespolone są reprezentowane przez krotkę(re,im).
# Gdzie:re-część rzeczywista liczby,im-częśćurojonaliczby.
# Proszę napisać podstawowe operacje na liczbach zespolonych ,m.in.dodawanie,
# odejmowanie, mnożenie, dzielenie, potęgowanie, wypisywanie i wczytywanie.
# ====================================================================================================>


def dodawanie(c1, c2): ...


def odejmowanie(c1, c2): ...


def mnozenie(c1, c2): ...


def dzielenie(c1, c2): ...


def potegowanie(c1, n): ...


def wypisywanie(c1): ...


def wczytywanie(): ...


if __name__ == "__main__":
    from testy125 import odpal_testy

    dodawanie(int(input("Podaj c1: ")), int(input("Podaj c2: ")))
    odejmowanie(int(input("Podaj c1: ")), int(input("Podaj c2: ")))
    mnozenie(int(input("Podaj c1: ")), int(input("Podaj c2: ")))
    dzielenie(int(input("Podaj c1: ")), int(input("Podaj c2: ")))
    potegowanie(int(input("Podaj c1: ")), int(input("Podaj n: ")))
    wypisywanie(int(input("Podaj c1: ")))

    # odpal_testy()
