from math import sqrt

def czy_pierwsza(n):
    if n==2 or n==3: return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0: return False
    else:
        i = 5
        while i < sqrt(n) + 1:
            if n % i == 0: return False
            i += 2
            if n % i == 0: return False
            i += 4
        #end while
    return True


def at_least_one_prime(tab):
    for i in range(0, len(tab) ):
        if czy_pierwsza( tab[i] ): return True
    #end for
    return False


def fibonacci_check(tab):
    a,b = 1,2
    if at_least_one_prime(tab):
        while a < len(tab):
            if czy_pierwsza( tab[a] ) : return False
            a, b = b, a+b
        #end while
    else:
        return False
    #end if
    return True


# --- main

tab = [12, 3, 8, 15, 4, 6]
print( fibonacci_check(tab) )

