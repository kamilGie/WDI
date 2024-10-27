import datetime
from random import randint

def sum_of_table(tab):
    n = len(tab)
    kolumny = [0]*n
    wiersze = [0]*n
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


def szachownica(tab):
    n = len(tab)
    kolumny, wiersze = sum_of_table(tab) # tablice z sumami poszczególnych wierszy i kolumn
    suma = 0
    best = 0

    for y in range(n-1): # y i x to wspolrzedne pierwszej wieży
        for x in range(n-1):
            for a in range(y+1, n): # a i b to wspolrzedne drugiej wiezy
                for b in range(x+1, n): # można dać range(n), ale wolniej to jest wtedy
                    if b != x:
                        suma = wiersze[y] + kolumny[x] + wiersze[a] + kolumny[b] - tab[y][b] - tab[a][x]
                        suma = suma - 2 * tab[y][x] - 2 * tab[a][b]
                    if suma > best:
                        best = suma
                        crd = ( [y,x], [a,b] )

    return best, crd


# --- main

tab = [ [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16] ]

print( szachownica(tab) )
# print( sum_of_table(tab) )




