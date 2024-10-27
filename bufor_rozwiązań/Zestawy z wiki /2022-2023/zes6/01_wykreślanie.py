from math import log10, floor, sqrt

# Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry

def reverse(n):
    new_number = 0
    while n > 0:
        new_number = 10 * new_number + n % 10
        n = n // 10
    #end while
    return new_number


def prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i <= sqrt( n ) + 1:
        if n % i == 0: return False
        else:
            i += 2
            if n % i == 0: return  False
            i += 4
    #end while
    return True


def liczba(n, w = 0):
    if n == 0:
        pom = reverse(w)
        if prime( pom ) and len( str(pom) ) >= 2: print( pom )
    else:

        liczba( n // 10, 10 * w + n % 10 )

        liczba( n // 10, w)




def find_all_primes(x):
    N = floor(log10(x)) + 1

    def rek(x, y, i):
        if x == 0:
            if i != N and i >= 2 and prime(y):
                print(y, i)
        else:
            rek(x//10, y, i)
            rek(x//10, y + (x % 10) * (10 ** i), i+1)

    rek(x, 0, 0)


find_all_primes(8231)
liczba(8231)

