from math import isqrt

def iloczyn_liczby(n):
    best = n-1
    iloczyn=(1,n)
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            suma = abs( n//i - i )
            if suma < best:
                best = suma
                iloczyn = (i, n//i)
    #end for
    return iloczyn

n = int( input() )
print( iloczyn_liczby(n) )