# ====================================================================================================>
# Zadanie 114
# Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami całkowitymi.
# Proszę zaimplementować funkcję chess(T) która ustawia na szachownicy dwie wieże, tak aby suma liczb na
# „szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna
# zwrócić położenie wież w postaci krotki (row ,col ,row ,col ).
# Uwaga: zakładamy, że pola na których znajdują się wieże nie są szachowane.
# Przykładowe wywołania funkcji:
# print(chess([[4,0,2],[3,0,0],[6,5,3]])) # (0,1,1,0) suma=17
# print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]] # (2,3,3,1) suma=35
# ====================================================================================================>
# chess((chess([[4,0,2],[3,0,0],[6,5,3]])))  --> return(x1,y1,x2,y2)
# tej sumy nie beda testy obejmowac same polozenia


# z wiki bledne bo liczy pola  dwurkotnie gdy wieze sa w tym samym wierzu/kolumnie


def sum_of_table(tab):
    n = len(tab)
    kolumny = [0] * n
    wiersze = [0] * n
    suma = 0

    for y in range(n):
        for x in range(n):
            suma += tab[y][x]
        wiersze[y] = suma
        suma = 0

    for x in range(n):
        for y in range(n):
            suma += tab[y][x]
        kolumny[x] = suma
        suma = 0

    return kolumny, wiersze


def chess(tab):
    n = len(tab)
    kolumny, wiersze = sum_of_table(tab)
    suma = 0
    best = float("-inf")
    best_positions = None

    for y in range(n):
        for x in range(n):
            for a in range(y + 1, n):
                for b in range(x + 1, n):
                    suma = (
                        wiersze[y]
                        + kolumny[x]
                        + wiersze[a]
                        + kolumny[b]
                        - tab[y][x]  # Pole, na którym stoi pierwsza wieża
                        - tab[a][b]  # Pole, na którym stoi druga wieża
                    )

                    if suma > best:
                        best = suma
                        best_positions = (y, x, a, b)

    return best_positions


if __name__ == "__main__":
    from Develop import stworz_zadanie

    stworz_zadanie([chess])
