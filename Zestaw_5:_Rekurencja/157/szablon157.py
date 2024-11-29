# ====================================================================================================>
# Zadanie 157
# Tablica T =[(x1,y1),(x1,y1),...] zawiera położenia N punktów o współrzędnych opisanych
# wartościami typu float .Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości
# 2 niepustych podzbiorów tego zbioru.
# ====================================================================================================>


def Zadanie_157(tablica) -> float: ...


if __name__ == "__main__":
    from testy157 import odpal_testy

    Zadanie_157(list(input("Podaj tablica: ")))

    # odpal_testy()
