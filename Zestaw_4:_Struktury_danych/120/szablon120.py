# ====================================================================================================>
# Zadanie 120
# Liczby wymierne są reprezentowane przez krotkę (l,m). Gdzie :l -liczba całkowita oznaczająca
# licznik, m-liczba naturalna oznaczająca mianownik. Proszę napisać podstawowe operacje na ułamkach,
# m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie.
# ====================================================================================================>


def skr(num): ...



def add(a, b): ...



def subtract(a, b): ...



def mult(a, b): ...



def div(a, b): ...



def exp(a, b): ...


if __name__ == "__main__":
    from testy120 import odpal_testy

    skr(int(input('Podaj num: ')))
    add(int(input('Podaj a: ')), int(input('Podaj b: ')))
    subtract(int(input('Podaj a: ')), int(input('Podaj b: ')))
    mult(int(input('Podaj a: ')), int(input('Podaj b: ')))
    div(int(input('Podaj a: ')), int(input('Podaj b: ')))
    exp(int(input('Podaj a: ')), int(input('Podaj b: ')))

    # odpal_testy()
