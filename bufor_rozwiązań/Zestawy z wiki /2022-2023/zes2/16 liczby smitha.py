from math import sqrt

def czy_pierwsza(n):
    if n==2 or n==3: return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0: return False
    else:
        i = 5
        while i < sqrt( n ) + 1:
            if n % i == 0: return False
            i += 2
            if n % i == 0: return False
            i += 4
        #end while
    return True

def suma_cyfr(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n = n // 10
    #end while
    return suma

def suma_rozkladu(n):
    suma = 0
    i = 2
    if czy_pierwsza(n): return suma_cyfr(n) + 1
    else:
        while n != 1:
            while n % i == 0:
                k = suma_cyfr( i )
                suma += k
                n //= i
            #end while
            i += 1
        #end while

    return suma

liczba = int( input() )

if suma_rozkladu( liczba ) == suma_cyfr( liczba ): print("Tak")
else: print("Nie")
