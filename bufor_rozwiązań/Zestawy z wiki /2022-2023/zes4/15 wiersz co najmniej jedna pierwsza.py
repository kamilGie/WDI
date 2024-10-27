from math import sqrt


def czy_zawiera(n):
    k = n
    primes = {2, 3, 5, 7}

    while k > 0:
        if ( k % 10 ) in primes: return True
        k = k // 10
    #end while
    return False


def czy_istnieje_wiersz(tab):
    n = len(tab)

    for y in range(n):
        flag = True
        for x in range(n):
            if not czy_zawiera( tab[y][x] ):
                flag = False
                break
        #end for 2
        if flag: return y, True
        flag = True
    #end for 1
    return False


tab = [ [14,12,13,962],
        [960,846,211,9],
        [666, 991, 484, 884],
        [645, 887, 666, 992] ]

print( czy_istnieje_wiersz(tab) )












