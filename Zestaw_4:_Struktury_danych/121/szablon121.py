# ====================================================================================================>
# zadanie 121
# używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą układ 2
# równań o 2 niewiadomych, w których współczynniki są liczbami wymiernymi
# ====================================================================================================>
# Układ równań:
# a1 * x + b1 * y = c1
# a2 * x + b2 * y = c2
# return (x,y)


def Zadanie_121(a1, b1, c1, a2, b2, c2) -> tuple: ...


if __name__ == "__main__":
    from testy121 import odpal_testy

    Zadanie_121(int(input('Podaj a1: ')), int(input('Podaj b1: ')), int(input('Podaj c1: ')), int(input('Podaj a2: ')), int(input('Podaj b2: ')), int(input('Podaj c2: ')))

    # odpal_testy()
