from random import randint

def if_only_odd(n):
    while n > 0:
        if ( n % 10) % 2 == 1: pass
        else: return False
        n = n // 10
    #end while
    return True

def odd_parity(tab, n):
    for element in tab:
        if if_only_odd( element ): return True
        else: pass
    #end for
    return False

# --- main

n = int( input() )
tab = [randint(1,1000) for _ in range(0, n) ]
print(tab)
print( odd_parity(tab, n) )