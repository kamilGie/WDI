from random import randint


def is_odd_number(n):
    while n > 0:
        if ( n % 10 ) % 2 == 1: return True
        else: n = n // 10
    #end while
    return False

def list_check(tab, n):
    for el in tab:
        if is_odd_number( el ): pass
        else: return "Nie zawiera", tab
    #end for
    return "Zawiera", tab

n = int( input() ) # n miejsc w tablicy
tab = [randint(1, 1000) for _ in range(0, n)]

print( list_check(tab, n) )
