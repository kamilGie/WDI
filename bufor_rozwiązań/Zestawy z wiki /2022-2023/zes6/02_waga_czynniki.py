from math import sqrt
from random import randint

def diff_div(n):
    k = n
    i = 2
    pom = 0
    cnt = 0
    while i <= sqrt(k) + 1:
        while n % i == 0:
            pom += 1
            n = n // i
        if pom > 0: cnt += 1
        pom = 0
        i += 1
    #end while
    return cnt




def wagi(t,a=0, b=0, c=0, n=0):
    if n == len(t) :
        return a == b == c
    else:
        return wagi(t, a+diff_div( t[n] ), b, c, n+1) or wagi(t, a, b+diff_div( t[n] ), c, n+1) or wagi(t, a, b, c+diff_div( t[n] ), n+1)


def waga(n):
    cnt = 0
    i = 2
    k = n 
    while i <= sqrt(k) + 1:
        if n % i == 0:
            cnt += 1
            while n % i == 0:
                n = n // i
        #end if 
        i += 1 
    #end while
    return cnt 

def zad2(T):
    
    def rek(x,y,z,i):
        if i == len(T):
            if x == y == z: return True 
            return False 
        else:
            return rek(x+waga( T[i] ), y, z, i + 1) or rek(x, y+waga( T[i] ), z, i + 1) or rek(x, y, z+waga( T[i] ), i + 1)
    #end def
    return rek(0,0,0,0)
#end zad2

T = [1,2,64,42,8,9,14,15]
print( zad2(T) )
print( wagi(T) )
