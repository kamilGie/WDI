def ulamek( l, m, n ):
    print( l // m , end="")
    i = 1

    if l % m != 0:
        print(".", end="")
        l = l % m
        while l > 0 and n > 0:
            l = l * 10
            print( l // m, end="")
            l = l % m
            n = n - 1
        #end while
    #end if
    return


def long_div(a, b, t):
    t[0] = a // b
    a = a % b
    for i in range(1, len(t) ):
        a = a * 10
        t[i] = a // b
        a = a % b
        if a == 0: return t
    #end for
    return t



def zad4(n):
    digits = [1] + [0]*( n )
    tab = [0] * ( n + 1 )
    fact = 1
    k = 1

    while fact <= 10**n + 1:
        fact *= k
        k += 1
        long_div(1, fact, tab)
        for i in range(n+1):
            digits[i] += tab[i]

    #end while
    for i in range( len(digits) - 1, 0, -1):
        digits[ i-1 ] += digits[i] // 10
        digits[i] %= 10
    #end for
    return digits [:n+1]








# --- main:
n = int(input())
t = [0] * (n+1)

print( zad4(n) )