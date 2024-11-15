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
# chess((chess([[4,0,2],[3,0,0],[6,5,3]])))  --> return(0,1,1,0)
# tej sumy nie beda testy obejmowac, same polozenia


import copy


def chess(tab):
    n = len(tab)
    best = float("-inf")
    best_positions = None

    for x in range(n):
        for y in range(n):

            suma_1 = 0
            tablica_z_wieza = copy.deepcopy(tab)
            tablica_z_wieza[x][y] = 0
            for x1 in range(0, n):
                suma_1 += tablica_z_wieza[x1][y]
                tablica_z_wieza[x1][y] = 0

            for y1 in range(0, n):
                suma_1 += tablica_z_wieza[x][y1]
                tablica_z_wieza[x][y1] = 0

            for a in range(x, n):
                for b in range(0, n):
                    if a == x and b == y:
                        continue
                    elif a == x or b == y:
                        suma_2 = -tab[a][b]
                    else:
                        suma_2 = 0

                    tablica_z_wieza[a][b] = 0

                    for a1 in range(0, n):
                        suma_2 += tablica_z_wieza[a1][b]

                    for b1 in range(0, n):
                        suma_2 += tablica_z_wieza[a][b1]

                    if suma_1 + suma_2 > best:
                        best = suma_2 + suma_1
                        best_positions = (x, y, a, b)

    return best_positions


