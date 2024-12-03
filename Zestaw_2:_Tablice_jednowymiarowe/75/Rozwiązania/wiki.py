# ====================================================================================================>
# Zadanie 75
# Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwraca-
# jącą wartość typu bool oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
# jeden element największy (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej
# wartości).
# ====================================================================================================>


def Zadanie_75(T):
    if len(T) < 1:
        return False

    min = max = T[0]
    min_jedyny = max_jedyny = True

    for el in T[1:]:
        if min > el:
            min = el
            min_jedyny = True
        elif min == el:
            min_jedyny = False

        if max < el:
            max = el
            max_jedyny = True
        elif max == el:
            max_jedyny = False

    return min_jedyny and max_jedyny


