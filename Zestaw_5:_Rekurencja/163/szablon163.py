# ====================================================================================================>
# Zadanie 163
# Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). Tablica T[N] za-
# wiera współrzędne N punktów leżących na płaszczyźnie. Punkty posiadają jednostkową masę. Proszę napisać
# funkcję,która sprawdza czy istnieje niepusty podzbiór n punktów, gdzie n¡k oraz n jest wielokrotnością liczby
# 3, którego środek ciężkości leży w odległości mniejszej niż r od początku układu współrzędnych. Do funkcji
# należy przekazać dokładnie 3 parametry: tablicę t, promień r, oraz ograniczenie k, funkcja powinna zwrócić
# wartość typu bool.
# ====================================================================================================>


def Zadanie_163(t, r, k): ...


if __name__ == "__main__":
    from testy163 import odpal_testy

    Zadanie_163( list(input("Podaj t: ")), float(input("Podaj r: ")), int(input("Podaj k: ")))

    # odpal_testy()
