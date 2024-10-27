# Proszę napisać program wypisujący podzielniki liczby

from math import sqrt

def divisors(n):
    if n==0:
        print("Każda liczba jest dzielnikiem")
        return

    i = 2
    while i*i < n:
        if n % i == 0:
            print(i, n//i, end=" ")
        #end if
        i+=1
    #end while

    if i*i == n: print(i, end=" ") # przypadek, gdy np. 11 * 11 = 121

    print(1,n, end=" ") # podzielnikami są także liczby 1 i "ta liczba"

n = int( input() )
divisors(n)





