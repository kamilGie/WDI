from random import randint


def f(T, w, k): # najtańsza ścieżka

    if w == 7:
        return T[w][k]


    if k > 0:
        left = f(T, w + 1, k - 1)
    else:
        left = float('inf')
    #end if

    if k < 7:
        right = f(T, w + 1, k + 1)
    else:
        right = float('inf')
    #end if

    middle = f(T, w + 1, k)

    return min( left, middle, right ) + T[w][k]





def zad3(T,k): # moje 
    best = float('inf')
    def rek(y, x, koszt):
        nonlocal best
        if y == 7: 
            best = min(best, koszt + T[y][x])
        else:
            if x > 0:
                rek(y + 1, x - 1, koszt + T[y][x] )

            rek(y + 1, x, koszt + T[y][x] )
            
            if x < 7: rek(y + 1, x + 1, koszt + T[y][x] ) 

    #end def rek
    rek(0, k, 0 )
    return best
#end zad3


T = [ [15, 17, 11, 15, 15, 19, 6, 9],
[20, 5, 18, 8, 15, 4, 4, 4],
[1, 14, 20, 16, 17, 17, 15, 17],
[14, 2, 2, 10, 20, 16, 15, 13],
[12, 18, 18, 12, 7, 4, 18, 1],
[19, 20, 18, 13, 16, 9, 2, 8],
[4, 9, 5, 6, 5, 5, 10, 4],
[2, 9, 10, 19, 19, 7, 8, 15] ]

print(zad3(T,3) ) 
print( f(T, 0, 3) )