# ====================================================================================================>
# Zadanie 158
# Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać
# na pola o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz
# funkcję, która sprawdza, czy da się przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie
# da, zwraca -1.
# ====================================================================================================>


def Zadanie_158(t): ...


if __name__ == "__main__":
    from testy158 import odpal_testy

    Zadanie_158(int(input('Podaj t: ')))

    # odpal_testy()
