# ====================================================================================================>
# Zadanie 113
# Dana jest tablica T[N][N] wypełniona wartościami 0,1. Każdy wiersz tablicy traktujemy
# jako liczbę zapisaną w systemie dwójkowy m o długości N bitów. Stała N jest rzędu 1000.
# Proszę zaimplementować funkcję distance(T), która dla takiej tablicy wyznaczy dwa wiersze, dla których różnica zawartych
# w wierszach liczb jest największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić odległość
# pomiędzy znalezionymi wierszami. Można założyć, że żadne dwa wiersze nie zawierają identycznego ciągu
# cyfr.
# ====================================================================================================>


def distance(T): ...


if __name__ == "__main__":
    from testy113 import odpal_testy

    distance(int(input('Podaj T: ')))

    # odpal_testy()
