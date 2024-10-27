from random import randint


def king_go(T, k):
    global min_sum
    king(T, k, 0, w = 0)

    return min_sum


def king(T, k, sum, w = 0):
    global min_sum

    if w == 7:
        min_sum = min(sum + T[w][k], min_sum)
    else:
        if k > 0:
            king(T, k - 1, sum + T[w][k], w + 1)
        #end if

        king(T, k, sum + T[w][k], w + 1)

        if k < 7:
            king(T, k + 1, sum + T[w][k], w + 1)
        #end if



min_sum = 10**10
T = [ [randint(1,40) for i in range(8) ] for i in range(8) ]
print( king_go(T, 2) )












