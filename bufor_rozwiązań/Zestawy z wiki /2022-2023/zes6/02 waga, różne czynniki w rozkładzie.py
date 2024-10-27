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
    if n == len(t) - 1:
        return a == b == c
    else:
        return wagi(t, a+diff_div( t[n] ), b, c, n+1) or wagi(t, a, b+diff_div( t[n] ), c, n+1) or wagi(t, a, b, c+diff_div( t[n] ), n+1)




t =  [randint(1,15) for i in range(11) ]
print( wagi(t) )