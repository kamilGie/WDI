from math import sqrt

def czynniki_pierwsze(n):
    b = 2
    while b <= sqrt(n):
        if n % b == 0:
            print(b)
            n = n // b
        else:
            b = b + 1
        #end if
    #end while
    if n > 1: print(n)


def sprawdz(T):
    n = len(T)
    T2 = [ False for _ in range(n) ]
    T2[0] = True

    for i in range(n):
        if T2[i]:
            temp = T[i]
            k = 2
            while temp != 1:
                while temp % k == 0:
                    if i + k < n:
                        T2[i+k] = True
                    temp = temp // k
                #end while 2
                k = k + 1
            #end while 1
    #end for
    return T2[n-1]

t = [6,1,5,2,4,3,9,6,1,2,4]
print( sprawdz(t) )
