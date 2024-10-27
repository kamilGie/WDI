from math import inf
from random import randint

def find_row(T, ixs):
    result = 0
    for i in range(1, len(T) ):
        if T[i][ ixs[i] ] < T[result][ ixs[result] ]:
            result = i
    #end for
    return result

def zad6(T1, T2):
    n = len( T1 )
    ixs = [ 0 for _ in range(n) ]
    prev = -1
    T2_ix = 0
    i = 0

    while i < n*n:
        row = find_row( T1, ixs )
        if T1[row][ ixs[row] ] != prev:
            prev = T2[ T2_ix ] = T1[row][ ixs[row] ]
            T2_ix += 1
        if ixs[row] == n - 1: T1[row][ ixs[row] ] = inf
        else: ixs[row] += 1
        i += 1
    #end while
    return T2


# --- main:

T1 = [ [1,2,3,4],
       [5,10,15,20],
       [69,70,80,102],
       [423,513,951,999] ]
T2 = [0] * 16

print( zad6(T1, T2) )