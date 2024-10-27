# do dokończenia

def sum_around(tab):
    best = 0
    n = len(tab)
    crd = (0,0)

    suma = tab[0][1] + tab[1][0]
    if suma > best:
        best = suma
        crd = (0,0)

    suma = tab[0][n-2] + tab[1][n-1]
    if suma > best:
        best = suma
        crd = (0, n-1)

    suma = tab[n-2][0] + tab[n - 1][1]
    if suma > best:
        best = suma
        crd = (n-1, 0)

    suma = tab[n-1][n - 2] + tab[n - 2][n-1]
    if suma > best:
        best = suma
        crd = (n-1, n-1)

    for y in range(1, n-1):
        for x in range(1, n-1):
            suma = tab[y-1][x] + tab[y][x-1] + tab[y][x+1] + tab[y+1][x]
            if suma > best:
                best = suma
                crd = (y,x)
        #end for 2
    #end for 1

    return best, crd


# --- main

tab = [ [100, 1,4],
        [9,3,9],
        [19,13,63]]

print( sum_around(tab) )






