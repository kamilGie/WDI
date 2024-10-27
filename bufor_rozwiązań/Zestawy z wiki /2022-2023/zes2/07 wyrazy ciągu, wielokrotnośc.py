from math import isqrt


def ciag(n):
    for i in range(1, isqrt(n)+1):
        an = i*i + i + 1
        if n % an ==0:
            return True
    #end for
    return False


n = int( input() )
print( ciag(n) )