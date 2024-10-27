from math import sqrt

def czy_pierwsza(n):
    if n < 2: return False
    if n==2 or n==3: return True
    if n%2==0 or n%3==0: return False
    else:
        i=5
        while i<sqrt(n)+1:

            if n%i==0: return False
            #end if

            i += 2

            if n%i==0: return False

            i+=4
        #end while
    return True

n = int( input() )
print( czy_pierwsza(n) )