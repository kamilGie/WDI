from math import sqrt



def same_cyfry_pierwsze(n):
    k = n
    primes = {2,3,5,7}
    while k > 0:
        if ( k % 10 ) not in primes: return False
        k = k // 10
    #end while
    return True


def wiersze_pierwsze(tab):
    n = len(tab)

    for y in range(n):
        flag = False
        for x in range(n):

            if same_cyfry_pierwsze( tab[y][x] ):
                flag = True
                break
            #end if

        #end for 2
        if not flag: return False

    #end for 1
    return True


# --- main

tab = [ [1,4,33,460],
        [614,583,22,913],
        [918,332,938,59183],
        [5981,301,33354,5913]]

print( wiersze_pierwsze(tab) )


