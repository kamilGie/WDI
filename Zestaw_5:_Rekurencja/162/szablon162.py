# ====================================================================================================>
# Zadanie 162
# Punkt leżący w przestrzeni jest opisywany trójką liczb typu float (x,y,z). Tablica T[N]
# zawiera współrzędne N punktów leżących w przestrzeni. Punkty posiadają jednostkową masę. Proszę napisać
# funkcję,która sprawdza czy istnieje podzbiór punktów liczący conajmniej 3 punkty, którego środek ciężkości
# leży w odległości nie większej niż r od początku układu współrzędnych. Do funkcji należy przekazać tablicę
# T oraz promień r, funkcja powinna zwrócić wartość typu bool.
# ====================================================================================================>


def Zadanie_162(t, r): ...


if __name__ == "__main__":
    from testy162 import odpal_testy

    Zadanie_162(int(input('Podaj t: ')), int(input('Podaj r: ')))

    # odpal_testy()
