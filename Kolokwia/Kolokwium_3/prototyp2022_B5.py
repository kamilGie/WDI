# ====================================================================================================>
# Zadanie B5, 19.01.2023
# Sudoku składa się kwadratu o wymiarach 9 × 9 podzielonego na 9 małych kwadratów o wymiarach 3 × 3.
# W poprawnym rozwiązaniu: w każdym wierszu, każdej kolumnie i każdym małym kwadracie znajdują się
# cyfry 1 − 9. W tablicy T[9][9] zawierającej poprawne rozwiązanie, ktoś je złośliwie uszkodził, zamieniając
# miejscami dwa małe kwadraty. Wiemy, że zamienione kwadraty leżały w różnych wierszach i różnych kolumnach. Zamiana spowodowała, że niektóre wiersze i niektóre kolumny zawierają powtarzające się cyfry.
# Proszę napisać funkcję repeair(T), która naprawi uszkodzoną tablicę. Do funkcji należy przekazać tablicę
# zawierającą uszkodzone rozwiązanie, funkcja powinna zwrócić informację czy zamiana dotyczyła środkowego
# małego kwadratu.
# Przykład: W poniższej tablicy zamieniono środkowy kwadrat z prawym dolnym.
#
# 8, 1, 2,  7, 5, 3,  6, 4, 9
# 9, 4, 3,  6, 8, 2,  1, 7, 5
# 6, 7, 5,  4, 9, 1,  2, 8, 3
#
# 1, 5, 4,  3, 6, 8,  8, 9, 6
# 3, 6, 9,  9, 1, 7,  7, 2, 1
# 2, 8, 7,  4, 5, 2,  5, 3, 4
#
# 5, 2, 1,  9, 7, 4,  2, 3, 7
# 4, 3, 8,  5, 2, 6,  8, 4, 5
# 7, 9, 6,  3, 1, 8,  1, 6, 9
# ====================================================================================================>


def Zadanie_B5(): ...


if __name__ == "__main__":
    from Develop import stworz_zadanie

    Zadanie_B5()
    # stworz_zadanie([Zadanie_B5])
