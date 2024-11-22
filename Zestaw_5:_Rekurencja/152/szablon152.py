# ====================================================================================================>
# Zadanie 152
# Zadanie jak powyżej. Funkcja sprawdzająca czy król może dostać się z pola w,k do które-
# gokolwiek z narożników.
# ====================================================================================================>


def Zadanie_152(board: list, x, y): ...


if __name__ == "__main__":
    from testy152 import odpal_testy

    Zadanie_152(int(input('Podaj board: ')), int(input('Podaj x: ')), int(input('Podaj y: ')))

    # odpal_testy()
