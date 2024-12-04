# ====================================================================================================>
# Zadanie 112
# Dana jest plansza o wymiarach NxN zawierająca wartości 0 i 1. Pola o wartości 1 zawierają
# pułapki.Skoczek musi dotrzeć z górnego wiersza planszy do dolnego. Każdy ruch skoczka musi go przybliżać do dolnego wiersza.
# Proszę napisać program, który zwraca długość najkrótszej bezpiecznej drogi skoczka z wiersza górnego do wiersza dolnego.
# ====================================================================================================>
# return dlugosci najkroszedj drogi  - jak sie da
# return False - jak sie nie da

# https://github.com/MarcinSerafin03/bit-algo-start-24-25-WDI/tree/main


def Zadanie_112(T):
    N = len(T)
    skoki = [(1, -2), (2, -1), (2, 1), (1, 2)]

    min_odległość = [[float("inf") if i > 0 else 0 for _ in range(N)] for i in range(N)]

    for y in range(N - 1):  # koordynaty
        for x in range(N):
            for skok in skoki:
                potencjalny_skok_y = y + skok[0]  # ładen nazwy
                potencjalny_skok_x = x + skok[1]
                # sprawdzenie czy potencjalny skok nie wyjdzie nam poza tablice
                if (
                    potencjalny_skok_y < 0
                    or potencjalny_skok_y > N - 1
                    or potencjalny_skok_x < 0
                    or potencjalny_skok_x > N - 1
                ):
                    continue
                # sprawdzanie czy możemy w ogóle skoczyć z tego pola (czy byliśmy wcześniej już)
                if min_odległość[y][x] == float("inf"):
                    continue
                # sprawdzenie czy nie ma miny
                if T[potencjalny_skok_y][potencjalny_skok_x] == 1:
                    continue
                min_odległość[potencjalny_skok_y][potencjalny_skok_x] = min(
                    min_odległość[y][x] + 1,
                    min_odległość[potencjalny_skok_y][potencjalny_skok_x],
                )

    result = float("inf")
    for i in range(N):
        result = min(min_odległość[N - 1][i], result)

    return result if result < float("inf") else False
