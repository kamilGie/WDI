# 1B.
# Sudoku składa się z kwadratu o wymiarach 9x9 podzielonego na 9 małych kwadratów
# o wymiarach 3x3.  Na potrzeby zadania, kolejne małe kwadraty numerujemy
# wierszami od 1 do 9.  W poprawnym rozwiązaniu w każdym wierszu, każdej
# kolumnie, i każdym małym kwadracie znajdują się liczby 1-9.  W poprawnym
# rozwiązaniu umieszczonym w tablicy T ktoś zamienił miejscami dwa małe kwadraty.
# Proszę napisać funkcję sudoku(T), która zwraca numery zamienionych kwadratów.
#
# Dla poniższych danych wejściowych, poprawną odpowiedzą jest krotka (5, 9).
#
# 8 1 2 7 5 3 6 4 9
# 9 4 3 6 8 2 1 7 5
# 6 7 5 4 9 1 2 8 3
# 1 5 4 3 6 8 8 9 6
# 3 6 9 9 1 7 7 2 1
# 2 8 7 4 5 2 5 3 4
# 5 2 1 9 7 4 2 3 7
# 4 3 8 5 2 6 8 4 5
# 7 9 6 3 1 8 1 6 9
#


def sudoku(T): ...


if __name__ == "__main__":
    from testy1b2023 import odpal_testy

    data = [
        [8, 1, 2, 7, 5, 3, 6, 4, 9],
        [9, 4, 3, 6, 8, 2, 1, 7, 5],
        [6, 7, 5, 4, 9, 1, 2, 8, 3],
        [1, 5, 4, 3, 6, 8, 8, 9, 6],
        [3, 6, 9, 9, 1, 7, 7, 2, 1],
        [2, 8, 7, 4, 5, 2, 5, 3, 4],
        [5, 2, 1, 9, 7, 4, 2, 3, 7],
        [4, 3, 8, 5, 2, 6, 8, 4, 5],
        [7, 9, 6, 3, 1, 8, 1, 6, 9],
    ]

    sudoku(data)

    # odpal_testy()
